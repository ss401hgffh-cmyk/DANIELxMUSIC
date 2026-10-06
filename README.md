# Saya Music

Telegram voice chat music bot for group playback with Pyrogram and PyTgCalls.

Maintainer: [SHNWAZDEV](https://t.me/kidzmc)
Demo Bot: [@Yorinamusicbot]([https://t.me/SexySayaBot](https://t.me/Yorinamusicbot))

## About

Saya Music is an advanced Telegram voice chat music bot with fast multi-source streaming, clean controls, and Railway-ready deployment.

## Topics

`music` `api` `docker` `telegram` `music-bot` `telegrambots` `shnwazdev` `railway` `pyrogram` `pytgcalls` `voice-chat` `streaming` `ffmpeg` `yt-dlp`

## Resources

- [Readme](README.md)

## License

- [MIT license](LICENSE)

## Security policy

- [Security policy](SECURITY.md)

## Activity

- Stars: ![GitHub Repo stars](https://img.shields.io/github/stars/shnwazdeveloper/saya-music?style=flat)
- Watchers: ![GitHub watchers](https://img.shields.io/github/watchers/shnwazdeveloper/saya-music?style=flat)
- Forks: ![GitHub forks](https://img.shields.io/github/forks/shnwazdeveloper/saya-music?style=flat)

## Overview

Saya Music supports audio and video playback in Telegram voice chats with queue controls, multi-source search, and admin tools.
It is designed for smooth group listening with easy setup on VPS, Docker, and Railway.

Tech stack:
- Python
- Pyrogram / Kurigram
- PyTgCalls
- MongoDB
- yt-dlp
- FFmpeg

## Features

- Voice chat streaming (audio and video)
- Queue management (play, skip, pause, resume, stop, seek, loop, shuffle)
- Source support: YouTube, Spotify, SoundCloud, Apple Music, Telegram files, direct links
- Group admin and utility commands
- Docker and Railway-ready deployment

## Required Environment Variables

```env
API_ID=
API_HASH=
OWNER_ID=
BOT_TOKEN=
MONGO_DB_URI=
LOGGER_ID=
```

## Recommended Environment Variables

```env
OWNER_USERNAME=
BOT_USERNAME=
BOT_NAME=Saya Music
STRING_SESSION=
COOKIE_URL=
API_URL=https://pvtz.nexgenbots.xyz
VIDEO_API_URL=https://api.video.nexgenbots.xyz
API_KEY=
DEEP_API=
SUPPORT_CHANNEL=
SUPPORT_CHAT=
UPSTREAM_REPO=https://github.com/shnwazdeveloper/saya-music
UPSTREAM_BRANCH=Master
```

Security note:
- Never commit real tokens, session strings, cookies, or database URIs.
- Store secrets only in `.env` or your deploy provider environment settings.

## Local Run

```bash
git clone https://github.com/shnwazdeveloper/saya-music
cd saya-music
python -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python -m SayaMusic
```

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m SayaMusic
```

## Deploy on Railway

1. Fork or push this repository.
2. Create a new Railway project from the repo.
3. Add environment variables from above.
4. Start command:

```bash
python -m SayaMusic
```

This service runs as a worker bot and does not need a public web port.

## Docker

```bash
cp sample.env .env
docker build -t saya-music .
docker run -d --name saya-music --env-file .env --restart unless-stopped saya-music
```
