import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Factily")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("gykmusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Taytlı")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "GottenYemeyenKalmasin")
PROJECT_NAME = getenv("PROJECT_NAME", "Gotten Yemeyen Kalmasın Music Bot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Taytl/VcPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "40"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
