from VillainMusic.core.bot import Nand
from VillainMusic.core.dir import dirr
from VillainMusic.core.git import git
from VillainMusic.core.userbot import Userbot
from VillainMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Nand()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
