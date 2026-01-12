"""
Video to Frames Extraction Script
Downloads videos (YouTube, LinkedIn, Facebook, X/Twitter, Reddit, etc.) and extracts a specified number of frames.

Requirements:
    pip install yt-dlp

Also requires ffmpeg to be installed and available in PATH.
"""

import os
import re
import subprocess
import sys
import argparse
import shutil
import unicodedata
import urllib.request
import urllib.parse
import hashlib
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser


def find_executable(name: str) -> str:
    """Find executable in PATH or common locations."""
    # First check if it's in PATH
    exe = shutil.which(name)
    if exe:
        return exe
    
    # Common paths to check
    search_paths = [
        # Python Scripts locations
        Path(sys.executable).parent / 'Scripts' / f'{name}.exe',
        Path(sys.executable).parent / f'{name}.exe',
        Path.home() / 'AppData' / 'Local' / 'Programs' / 'Python' / 'Python311' / 'Scripts' / f'{name}.exe',
        Path.home() / 'AppData' / 'Local' / 'Programs' / 'Python' / 'Python310' / 'Scripts' / f'{name}.exe',
        Path.home() / 'AppData' / 'Local' / 'Programs' / 'Python' / 'Python312' / 'Scripts' / f'{name}.exe',
    ]
    
    # Add ffmpeg/ffprobe specific paths (winget installation)
    if name in ['ffmpeg', 'ffprobe', 'ffplay']:
        winget_dir = Path.home() / 'AppData' / 'Local' / 'Microsoft' / 'WinGet' / 'Packages'
        if winget_dir.exists():
            for pkg_dir in winget_dir.iterdir():
                if 'FFmpeg' in pkg_dir.name:
                    for bin_path in pkg_dir.rglob(f'{name}.exe'):
                        search_paths.insert(0, bin_path)
                        break
    
    for path in search_paths:
        if path.exists():
            return str(path)
    
    return name  # Return original name as fallback


# =============================================================================
# WEB SCRAPING FALLBACK MODULE
# Used when yt-dlp fails (e.g., for YapFiles, obscure video hosts)
# =============================================================================

class VideoURLParser(HTMLParser):
    """HTML Parser to extract video URLs from page content."""
    
    def __init__(self):
        super().__init__()
        self.video_urls = []
        self.title = None
        self.in_title = False
        self.og_title = None
        self.og_description = None
    
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Extract from <video> and <source> tags
        if tag in ('video', 'source'):
            src = attrs_dict.get('src', '')
            if src and self._is_video_url(src):
                self.video_urls.append(src)
        
        # Extract from <a> tags that might be download links
        if tag == 'a':
            href = attrs_dict.get('href', '')
            if href and self._is_video_url(href):
                self.video_urls.append(href)
        
        # Track title tag
        if tag == 'title':
            self.in_title = True
        
        # Extract OpenGraph metadata
        if tag == 'meta':
            prop = attrs_dict.get('property', attrs_dict.get('name', ''))
            content = attrs_dict.get('content', '')
            if prop == 'og:title' and content:
                self.og_title = content
            elif prop == 'og:description' and content:
                self.og_description = content
    
    def handle_data(self, data):
        if self.in_title and data.strip():
            self.title = data.strip()
    
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
    
    def _is_video_url(self, url: str) -> bool:
        """Check if URL looks like a video file."""
        video_extensions = ('.mp4', '.webm', '.mkv', '.avi', '.mov', '.m4v', '.flv')
        url_lower = url.lower().split('?')[0]
        return any(url_lower.endswith(ext) for ext in video_extensions)


def scrape_video_urls(page_url: str) -> tuple:
    """
    Scrape a webpage to find direct video URLs.
    
    Returns:
        tuple: (list of video URLs, page HTML, parsed metadata)
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': page_url
    }
    
    try:
        req = urllib.request.Request(page_url, headers=headers)
        response = urllib.request.urlopen(req, timeout=30)
        html = response.read().decode('utf-8', errors='replace')
    except Exception as e:
        raise RuntimeError(f"Failed to fetch page: {e}")
    
    # Parse HTML for video tags
    parser = VideoURLParser()
    try:
        parser.feed(html)
    except:
        pass  # HTML parsing can fail on malformed pages
    
    video_urls = list(set(parser.video_urls))  # Deduplicate
    
    # Also search with regex patterns for URLs not in standard tags
    patterns = [
        r'https?://[^\s"\'<>]+/files/[^\s"\'<>]+\.mp4[^\s"\'<>]*',
        r'https?://[^\s"\'<>]+\.(?:mp4|webm|mkv|m4v)[^\s"\'<>]*',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, html, re.IGNORECASE)
        for match in matches:
            clean_url = re.sub(r'[\]\)\'"<>]+$', '', match)
            clean_url = clean_url.replace('&amp;', '&')
            if clean_url not in video_urls:
                video_urls.append(clean_url)
    
    metadata = {
        'title': parser.og_title or parser.title or 'Unknown Video',
        'description': parser.og_description or '',
        'source_url': page_url
    }
    
    return video_urls, html, metadata


def generate_video_id_from_url(url: str) -> str:
    """Generate a unique video ID from URL."""
    path = urllib.parse.urlparse(url).path
    parts = [p for p in path.split('/') if p]
    
    for part in reversed(parts):
        part = re.sub(r'\.(mp4|webm|mkv|html|htm)$', '', part, flags=re.IGNORECASE)
        if re.match(r'^[a-zA-Z0-9_-]{6,}$', part):
            return part[:20]
    
    return hashlib.md5(url.encode()).hexdigest()[:12]


def download_video_direct(video_url: str, output_path: Path, referer: str = None) -> Path:
    """Download video directly via HTTP with proper headers."""
    output_path = output_path.resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    
    output_file = output_path / 'downloaded_video.mp4'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    if referer:
        headers['Referer'] = referer
    
    try:
        req = urllib.request.Request(video_url, headers=headers)
        print(f"  [SCRAPE] Downloading from: {video_url[:80]}...")
        
        with urllib.request.urlopen(req, timeout=120) as response:
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' in content_type:
                raise RuntimeError("URL returned HTML instead of video")
            
            total_size = int(response.headers.get('Content-Length', 0))
            downloaded = 0
            chunk_size = 1024 * 1024
            
            with open(output_file, 'wb') as f:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        pct = (downloaded / total_size) * 100
                        print(f"\r  [SCRAPE] Downloaded: {downloaded / (1024*1024):.1f}MB / {total_size / (1024*1024):.1f}MB ({pct:.0f}%)", end='')
            print()
        
        if output_file.exists() and output_file.stat().st_size > 10000:
            print(f"  [SCRAPE] Video saved to: {output_file}")
            return output_file
        else:
            raise RuntimeError("Downloaded file is too small")
            
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"URL Error: {e.reason}")


def scrape_video_info(url: str) -> dict:
    """Get video info by scraping the page (fallback when yt-dlp fails)."""
    print(f"  [SCRAPE] Fetching page metadata...")
    
    video_urls, html, metadata = scrape_video_urls(url)
    video_id = generate_video_id_from_url(url)
    
    return {
        'title': metadata['title'],
        'duration': 'unknown',
        'id': video_id,
        'uploader': 'Unknown (scraped)',
        'upload_date': datetime.now().strftime('%Y%m%d'),
        'url': url,
        '_scraped': True,
        '_video_urls': video_urls,
        '_referer': url
    }


def sanitize_filename(name: str, video_id: str = None) -> str:
    """
    Robustly sanitize a filename for Windows filesystem.
    
    Args:
        name: The original filename/title to sanitize
        video_id: Optional video ID to use as fallback or suffix
        
    Returns:
        A safe, valid Windows filename
    """
    if not name:
        return f"video_{video_id}" if video_id else "video_frames"
    
    # Normalize unicode characters (e.g., convert fancy characters to ASCII equivalents)
    name = unicodedata.normalize('NFKD', name)
    
    # Keep only ASCII letters, numbers, spaces, underscores, and hyphens
    sanitized = ""
    for char in name:
        if char.isascii() and (char.isalnum() or char in ' _-'):
            sanitized += char
        elif char == ' ':
            sanitized += ' '  # Keep spaces
    
    # Replace multiple spaces/underscores/hyphens with single space
    sanitized = re.sub(r'[\s_-]+', ' ', sanitized)
    
    # Trim whitespace
    sanitized = sanitized.strip()
    
    # Windows doesn't allow trailing dots or spaces in folder names
    sanitized = sanitized.rstrip('. ')
    
    # Restricted Windows names
    restricted = ['CON', 'PRN', 'AUX', 'NUL', 
                  'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 
                  'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
    if sanitized.upper() in restricted:
        sanitized = f"{sanitized}_video"
    
    # If name is too short (less than 3 chars) or empty after sanitization, use video_id
    if len(sanitized) < 3:
        if video_id:
            sanitized = f"video_{video_id}"
        else:
            sanitized = "video_frames"
    
    # Limit folder name length to avoid Windows path length issues (keep ID space)
    max_title_length = 60
    if len(sanitized) > max_title_length:
        sanitized = sanitized[:max_title_length].strip()
    
    # Always append video_id for uniqueness and traceability if provided
    if video_id:
        sanitized = f"{sanitized}_{video_id}"
    
    return sanitized


def get_video_info(url: str, force_scrape: bool = False, cookies_from_browser: str = 'firefox') -> dict:
    """Get video title and duration using yt-dlp, with scraping fallback."""
    
    if force_scrape:
        print("  [INFO] Force scrape mode - skipping yt-dlp")
        return scrape_video_info(url)
    
    ytdlp_exe = find_executable('yt-dlp')
    
    # List of browsers to try in order if the specified/default one fails
    browsers_to_try = [cookies_from_browser] if cookies_from_browser else ['firefox', 'chrome', 'edge']
    if cookies_from_browser and cookies_from_browser not in ['firefox', 'chrome', 'edge']:
        browsers_to_try.extend(['firefox', 'chrome', 'edge'])
    
    # Deduplicate while preserving order
    browsers_to_try = list(dict.fromkeys([b for b in browsers_to_try if b]))
    
    last_error = None
    
    for browser in browsers_to_try:
        try:
            print(f"  [INFO] Attempting to get info using {browser} cookies...")
            cmd = [ytdlp_exe, '--remote-components', 'ejs:github', '--print', '%(title)s', '--print', '%(duration)s', '--print', '%(id)s', '--print', '%(uploader)s', '--print', '%(upload_date)s']
            cmd.extend(['--cookies-from-browser', browser])
            cmd.append(url)
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            lines = result.stdout.strip().split('\n')
            title = lines[0] if lines else 'video'
            duration = lines[1] if len(lines) > 1 else '0:00'
            video_id = lines[2] if len(lines) > 2 else 'unknown'
            uploader = lines[3] if len(lines) > 3 else 'Unknown Uploader'
            upload_date = lines[4] if len(lines) > 4 else 'Unknown Date'
            
            if not video_id or video_id == 'NA':
                video_id = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            return {
                'title': title, 
                'duration': duration, 
                'id': video_id, 
                'uploader': uploader, 
                'upload_date': upload_date,
                'url': url,
                '_used_browser': browser
            }
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            error_msg = e.stderr if hasattr(e, 'stderr') else str(e)
            print(f"  [WARN] yt-dlp with {browser} failed: {error_msg[:100]}...")
            last_error = e
            # Continue to next browser
    
    print("  [INFO] All browser cookie attempts failed. Trying without cookies...")
    try:
        cmd = [ytdlp_exe, '--remote-components', 'ejs:github', '--print', '%(title)s', '--print', '%(duration)s', '--print', '%(id)s', '--print', '%(uploader)s', '--print', '%(upload_date)s', url]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        return {
            'title': lines[0], 'duration': lines[1], 'id': lines[2], 
            'uploader': lines[3], 'upload_date': lines[4], 'url': url
        }
    except Exception:
        print("  [INFO] Falling back to web scraping...")
        return scrape_video_info(url)


def download_video(url: str, output_path: Path, cookies_from_browser: str = 'firefox') -> Path:
    """Download video using yt-dlp with robust path handling."""
    ytdlp_exe = find_executable('yt-dlp')
    
    # Ensure output path is absolute and exists
    output_path = output_path.resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Use a simple, fixed output filename to avoid path issues
    output_file = output_path / 'downloaded_video.mp4'
    
    # Browsers to try (same logic as info)
    browsers_to_try = [cookies_from_browser] if cookies_from_browser else ['firefox', 'chrome', 'edge']
    if cookies_from_browser and cookies_from_browser not in ['firefox', 'chrome', 'edge']:
        browsers_to_try.extend(['firefox', 'chrome', 'edge'])
    browsers_to_try = list(dict.fromkeys([b for b in browsers_to_try if b]))

    for browser in browsers_to_try:
        try:
            print(f"  [DOWNLOAD] Attempting download using {browser} cookies...")
            cmd = [
                    ytdlp_exe,
                    '--remote-components', 'ejs:github',
                    '--ignore-config',
                    '--no-cache-dir',
                    '--no-part',
                    '-f', 'best[height<=720]/best',
                    '-o', str(output_file),
                    '--no-playlist',
                    '--restrict-filenames',
                    '--cookies-from-browser', browser,
                    url
                ]
            
            subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=str(output_path))
            
            if output_file.exists():
                print(f"  [DOWNLOAD] Video saved to: {output_file}")
                return output_file
        except subprocess.CalledProcessError:
            continue

    # Final attempt without cookies
    try:
        print(f"  [DOWNLOAD] Attempting download without cookies...")
        cmd = [ytdlp_exe, '--remote-components', 'ejs:github', '--no-part', '-f', 'best[height<=720]/best', '-o', str(output_file), '--restrict-filenames', url]
        subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=str(output_path))
        if output_file.exists(): return output_file
    except Exception:
        pass

    # Fallback to looking for any video file
    video_extensions = ['.mp4', '.webm', '.mkv', '.avi', '.mov']
    for file in output_path.iterdir():
        if file.suffix.lower() in video_extensions:
            return file
    
    raise FileNotFoundError(f"Downloaded video not found in {output_path}")


def get_video_duration_seconds(video_path: Path) -> float:
    """Get video duration in seconds using ffprobe."""
    ffprobe_exe = find_executable('ffprobe')
    
    try:
        result = subprocess.run(
            [
                ffprobe_exe,
                '-v', 'error',
                '-show_entries', 'format=duration',
                '-of', 'default=noprint_wrappers=1:nokey=1',
                str(video_path)
            ],
            capture_output=True,
            text=True,
            check=True
        )
        return float(result.stdout.strip())
    except (subprocess.CalledProcessError, ValueError) as e:
        raise RuntimeError(f"Error getting video duration: {e}")


def extract_frames(video_path: Path, output_dir: Path, num_frames: int, video_id: str) -> int:
    """
    Extract evenly spaced frames from video using ffmpeg.
    
    Returns:
        Number of frames actually extracted
    """
    ffmpeg_exe = find_executable('ffmpeg')
    
    # Ensure output directory is absolute and exists
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get video duration
    duration = get_video_duration_seconds(video_path)
    
    # Calculate frame rate to get desired number of frames
    fps = num_frames / duration
    
    output_pattern = str(output_dir / f'frame_%04d_{video_id}.jpg')
    
    print(f"  [EXTRACT] Extracting {num_frames} frames from {duration:.2f}s video...")
    print(f"  [EXTRACT] Output directory: {output_dir}")
    
    try:
        subprocess.run(
            [
                ffmpeg_exe,
                '-i', str(video_path),
                '-vf', f'fps={fps}',
                '-q:v', '2',  # High quality JPEG
                output_pattern,
                '-y'  # Overwrite existing files
            ],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Count actual extracted frames
        frame_count = len(list(output_dir.glob(f'frame_*_{video_id}.jpg')))
        print(f"  [EXTRACT] Successfully extracted {frame_count} frames")
        
        return frame_count
        
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error extracting frames: {e.stderr}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: ffmpeg not found at '{ffmpeg_exe}'. Please install ffmpeg and add to PATH.")


def generate_credits(info: dict, output_dir: Path) -> None:
    """Generate a CREDITS.txt file with attribution and legal disclaimer."""
    credits_path = output_dir / "CREDITS.txt"
    
    legal_disclaimer = """--- FAIR USE & OWNERSHIP DISCLAIMER ---
This dataset and its contents may contain copyrighted material obtained from public sources, the use of which has not always been specifically authorized by the copyright owner. 

Section 107 of the U.S. Copyright Act (the "Fair Use" provision) permits the limited use of copyrighted material without requiring permission from the rights holders for purposes such as criticism, commentary, news reporting, teaching, scholarship, and research.

We believe the extraction, processing, and preservation of these frames for research, archival, and data analysis purposes constitutes "fair use". This use is intended to be transformative, contributing new insights beyond the scope of the original work.

INTELLECTUAL PROPERTY NOTICE:
While original copyright for the video content remains with the respective holders, all rights to the software, extraction methodology, processing algorithms, and the resulting organized dataset/newly generated derivative content are the exclusive property of this project. 

Attribution for the original source material is provided below.
"""
    
    content = f"""
VIDEO CREDITS
=============
Title: {info['title']}
Video ID: {info['id']}
Original URL: {info['url']}
Uploader: {info['uploader']}
Upload Date: {info['upload_date']}

{legal_disclaimer}

If you wish to use copyrighted material from this folder for purposes of your own that go beyond "fair use," you must obtain permission from the copyright owner.
"""
    
    with open(credits_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    
    print(f"  [CREDITS] Generated: {credits_path}")


def process_video(url: str, num_frames: int = 300, base_dir: Path = None, force_scrape: bool = False, keep_video: bool = False, cookies_from_browser: str = 'firefox') -> bool:
    """
    Process a single video: download, extract frames, generate credits.
    
    Args:
        url: Video URL to process
        num_frames: Number of frames to extract
        base_dir: Base output directory (default: ./Output)
        force_scrape: If True, bypass yt-dlp and use web scraping
        keep_video: If True, keep the downloaded video file after extraction
        cookies_from_browser: Browser to extract cookies from (default: 'firefox')
        
    Returns:
        True if successful, False otherwise
    """
    # Establish base directory with absolute path
    if base_dir is None:
        script_dir = Path(__file__).resolve().parent
        base_dir = script_dir / "Output"
    else:
        base_dir = Path(base_dir).resolve()
    
    base_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Processing: {url}")
    print(f"{'='*60}")
    
    try:
        # Step 1: Get video info
        print("\n[1/4] Getting video information...")
        info = get_video_info(url, force_scrape=force_scrape, cookies_from_browser=cookies_from_browser)
        title = info['title']
        video_id = info['id']
        
        # Safe print for Windows console (encode to ASCII with replacement)
        safe_title = title.encode('ascii', 'replace').decode('ascii')
        print(f"  Title: {safe_title}")
        print(f"  Video ID: {video_id}")
        
        # Step 2: Create output directory with sanitized name + video ID
        folder_name = sanitize_filename(title, video_id)
        output_dir = (base_dir / folder_name).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n[2/4] Created output folder:")
        print(f"  {output_dir}")
        
        # Step 3: Download video
        print("\n[3/4] Downloading video...")
        
        # Use scraped video URLs if available (from fallback scraping)
        if info.get('_scraped') and info.get('_video_urls'):
            video_urls = info['_video_urls']
            referer = info.get('_referer', url)
            print(f"  [SCRAPE] Found {len(video_urls)} video URL(s) to try")
            
            video_path = None
            for i, video_url in enumerate(video_urls[:5]):  # Try up to 5 URLs
                try:
                    print(f"  [SCRAPE] Attempting URL {i+1}/{min(len(video_urls), 5)}...")
                    video_path = download_video_direct(video_url, output_dir, referer)
                    break
                except Exception as e:
                    print(f"  [SCRAPE] URL {i+1} failed: {str(e)[:50]}")
            
            if video_path is None:
                raise RuntimeError("All scraped video URLs failed to download")
        else:
            video_path = download_video(url, output_dir, cookies_from_browser=cookies_from_browser)
        
        if not video_path.exists():
            raise FileNotFoundError(f"Video file not found at {video_path}")
        
        # Step 4: Generate Credits/Compliance info
        generate_credits(info, output_dir)
        
        # Step 5: Extract frames (directly into output_dir, not nested)
        print(f"\n[4/4] Extracting {num_frames} frames...")
        frame_count = extract_frames(video_path, output_dir, num_frames, video_id)
        
        # Step 6: Cleanup - optionally remove the downloaded video
        if keep_video:
            print(f"  [KEEP] Video preserved at: {video_path}")
        else:
            try:
                video_path.unlink()
                print(f"  [CLEANUP] Removed temporary video file")
            except Exception as e:
                print(f"  [CLEANUP] Could not remove video file: {e}")
        
        # Final summary
        print(f"\n{'='*60}")
        print(f"SUCCESS: {safe_title}")
        print(f"  Folder: {output_dir}")
        print(f"  Frames: {frame_count}")
        print(f"{'='*60}")
        
        return True
        
    except Exception as e:
        print(f"\n{'='*60}")
        print(f"ERROR processing: {url}")
        print(f"  {type(e).__name__}: {str(e)}")
        print(f"{'='*60}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Download video and extract frames',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python video_to_frames.py "https://www.youtube.com/watch?v=VIDEO_ID"
    python video_to_frames.py "https://www.linkedin.com/posts/..."
    python video_to_frames.py "https://x.com/user/status/123456789"
    python video_to_frames.py "https://www.reddit.com/r/subreddit/comments/abc123/title/"
    python video_to_frames.py "URL1" "URL2" "URL3" --frames 50
        """
    )
    
    parser.add_argument('urls', nargs='+', help='Video URL(s) (YouTube, LinkedIn, Facebook, X/Twitter, Reddit, etc.)')
    parser.add_argument(
        '--frames', '-f',
        type=int,
        default=300,
        help='Number of frames to extract (default: 300)'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        default=None,
        help='Output directory (default: ./Output)'
    )
    parser.add_argument(
        '--force-scrape', '-s',
        action='store_true',
        help='Bypass yt-dlp and use web scraping (for sites yt-dlp cannot handle)'
    )
    parser.add_argument(
        '--keep-video', '-k',
        action='store_true',
        help='Keep the downloaded video file after frame extraction'
    )
    parser.add_argument(
        '--cookies-from-browser', '-c',
        type=str,
        default='firefox',
        help='Extract cookies from browser (default: firefox, then fallback to chrome, edge)'
    )
    
    args = parser.parse_args()
    
    print(f"\n{'#'*60}")
    print(f"Video to Frames Extraction")
    print(f"Processing {len(args.urls)} video(s), {args.frames} frames each")
    print(f"{'#'*60}")
    
    success_count = 0
    total_count = len(args.urls)
    
    for i, url in enumerate(args.urls, 1):
        print(f"\n[{i}/{total_count}]")
        if process_video(url, args.frames, args.output, args.force_scrape, args.keep_video, args.cookies_from_browser):
            success_count += 1
    
    print(f"\n{'#'*60}")
    print(f"BATCH COMPLETE")
    print(f"Successfully processed {success_count} of {total_count} videos")
    print(f"{'#'*60}\n")
    
    if success_count < total_count:
        sys.exit(1)


if __name__ == '__main__':
    main()
