import os
from pathlib import Path
from video_to_frames import get_video_info, generate_credits

def backfill():
    urls = [
        "https://www.youtube.com/watch?v=z7_gOkeN3eg",
        "https://www.youtube.com/watch?v=NeSQIFsMa7U",
        "https://www.youtube.com/watch?v=sinnEYiNg8k",
        "https://www.youtube.com/watch?v=oTB1EsrAi1Q",
        "https://www.youtube.com/watch?v=QrfaW880mLE",
        "https://www.youtube.com/watch?v=tCCM99wOBXA",
        "https://www.youtube.com/shorts/SH4BSLT-Df8",
        "https://www.youtube.com/shorts/IvRI52UF4Cw",
        "https://www.youtube.com/shorts/xFDFaclpK9g"
    ]
    
    output_base = Path("Output")
    
    # Also check the root directory for legacy extractions
    root_dir = Path(".")
    
    for url in urls:
        print(f"Processing: {url}")
        try:
            info = get_video_info(url)
            title = info['title']
            
            # Find the corresponding folder
            # We look for folders matching the title (sanitized)
            from video_to_frames import sanitize_filename
            sanitized = sanitize_filename(title)
            
            # Handle the specific case for Geran-2
            if sanitized == "-2":
                folder_name = "Geran-2_Production_Overview"
            else:
                folder_name = sanitized
            
            if len(folder_name) > 80:
                folder_name = folder_name[:80].strip()
            
            # Possible locations
            possible_paths = [
                output_base / folder_name,
                root_dir / folder_name
            ]
            
            found = False
            for p in possible_paths:
                if p.exists() and p.is_dir():
                    print(f"Found folder: {p}")
                    generate_credits(info, p)
                    found = True
                    break
            
            if not found:
                print(f"Could not find folder for: {title}")
                
        except Exception as e:
            print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    backfill()
