# Video to Frames Extraction Tool

A robust Python script for downloading videos from various platforms and extracting frames for dataset creation.

## Features

- **Multi-Platform Support**: YouTube, LinkedIn, X/Twitter, Reddit, Facebook, and 1000+ sites via yt-dlp
- **Robust Filename Handling**: Sanitizes special characters, ensures unique folder names with video IDs
- **Batch Processing**: Process multiple URLs in a single command
- **Automatic Credits**: Generates `CREDITS.txt` with attribution and fair use disclaimer
- **High Quality Frames**: Extracts evenly-spaced JPEG frames at configurable count

## Requirements

### Dependencies
```bash
pip install yt-dlp
```

### External Tools
- **FFmpeg**: Required for frame extraction
  ```bash
  # Windows (winget)
  winget install FFmpeg
  
  # Or download from https://ffmpeg.org/download.html
  ```

## Usage

### Basic Usage
```bash
# Extract 300 frames (default) from a video
python video_to_frames.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Extract from LinkedIn
python video_to_frames.py "https://www.linkedin.com/posts/..."

# Extract from X/Twitter
python video_to_frames.py "https://x.com/user/status/1234567890"

# Extract from Reddit
python video_to_frames.py "https://www.reddit.com/r/subreddit/comments/abc123/title/"
```

### Custom Frame Count
```bash
# Extract 50 frames
python video_to_frames.py "URL" --frames 50

# Short form
python video_to_frames.py "URL" -f 50
```

### Batch Processing
```bash
# Process multiple videos
python video_to_frames.py "URL1" "URL2" "URL3" --frames 30
```

### Custom Output Directory
```bash
python video_to_frames.py "URL" --output "D:\MyDataset"
```

## Output Structure

```
Output/
├── Video Title Here_abc123def/
│   ├── CREDITS.txt              # Attribution & legal info
│   ├── frame_0001_abc123def.jpg
│   ├── frame_0002_abc123def.jpg
│   └── ...
└── Another Video_xyz789ghi/
    ├── CREDITS.txt
    └── ...
```

**Naming Convention**: `{sanitized_title}_{video_id}/`
- Ensures uniqueness even with similar titles
- Video ID enables traceability to source

## Troubleshooting

### "yt-dlp not found"
```bash
pip install yt-dlp
# Or update existing installation
pip install -U yt-dlp
```

### "ffmpeg not found"
Ensure FFmpeg is installed and in your PATH:
```bash
ffmpeg -version
```

### Video download fails
- Update yt-dlp: `pip install -U yt-dlp`
- Some platforms may require authentication or have restrictions

## License

MIT License - See source code for details.
