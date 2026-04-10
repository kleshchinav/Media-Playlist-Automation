# Media Playlist Automation (VLC)

Automation tool for managing video playlists in a shared network environment.

## Overview

This script monitors a shared directory with media files, automatically generates a playlist, and controls VLC playback.

Designed for use cases like:
- Office TV screens
- Digital signage
- Internal media broadcasting

## Features

- Automatic playlist generation from network directory
- Scheduled daily restart of playback
- Fullscreen VLC playback
- Looping media
- Handles dynamic file updates
- Minimal UI (background automation)

## Tech Stack

- Python
- VLC media player
- schedule

## How It Works

1. Scans a network folder for video files
2. Generates `.m3u` playlist
3. Starts VLC in fullscreen mode
4. Restarts playback ежедневно по расписанию

## Notes

- Network paths and internal infrastructure details are anonymized
- Designed for Windows environment

## Author

Aleksandr Kleshchin  
IT Support Manager / System Administrator
