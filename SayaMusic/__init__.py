# Saya Music
from SayaMusic.core.bot import MusicBotClient
from SayaMusic.core.dir import StorageManager
from SayaMusic.core.git import git
from SayaMusic.core.userbot import Userbot
from SayaMusic.misc import dbb

from .logging import LOGGER

StorageManager()
git()
dbb()

app = MusicBotClient()
userbot = Userbot()


from .platforms import AppleAPI, CarbonAPI, RessoAPI, SoundAPI, SpotifyAPI, TeleAPI, YouTubeAPI

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

__all__ = [
    "LOGGER",
    "app",
    "userbot",
    "Apple",
    "Carbon",
    "SoundCloud",
    "Spotify",
    "Resso",
    "Telegram",
    "YouTube",
]
