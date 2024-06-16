import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# ------------------------------------------------------
BOT_TOKEN = getenv("7064273182:AAHPtqoAGpEw1revx2I__Ru0YCZC_QZfztU")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","ITZ_IND_CODER")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "DevilXmusicrobot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "DEVIL")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "IDK")
# ---------------------------------------------------------
# ---------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002114104208))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 6648419852))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/INDIANCODERS-1/SHUKLA-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/INDIAN_CODER_CC_GIVEAWAY")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/the_ind_coders")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQDF_T8AE3qJkEvDbivobqAJoTf1GMCz4niRImvF0U2_CPJbmA7EgJxNfEIx0MEkCt5wz4TMp8YdzU6u1GNYrDuIdycmpXcl81Xca001a6Z02CxhhqVJwGe0IZUiRCOjIDCH8Z8ENZJ_Sovpw0cw320ChEE2J9635Pvm3h6cox1PWDkvfl1KwtSkSu83nBmkh7YN3Pbz9kffmOJQ7W4314N88dT51AcUV-OPK3dtpy0KYSR6GXYwMS3UwdV8ucagfHXm2EpMgME6qVs1_Z6TScx4_YU9hq6qElq4ydkdcaTT73NlKXw4Pgn72OaEbMeuLSCQGfvZA_RNpEI8DyZN_qEXQZmx4QAAAAGilCGTAA")
STRING2 = getenv("STRING_SESSION2", "BQDF_T8AE3qJkEvDbivobqAJoTf1GMCz4niRImvF0U2_CPJbmA7EgJxNfEIx0MEkCt5wz4TMp8YdzU6u1GNYrDuIdycmpXcl81Xca001a6Z02CxhhqVJwGe0IZUiRCOjIDCH8Z8ENZJ_Sovpw0cw320ChEE2J9635Pvm3h6cox1PWDkvfl1KwtSkSu83nBmkh7YN3Pbz9kffmOJQ7W4314N88dT51AcUV-OPK3dtpy0KYSR6GXYwMS3UwdV8ucagfHXm2EpMgME6qVs1_Z6TScx4_YU9hq6qElq4ydkdcaTT73NlKXw4Pgn72OaEbMeuLSCQGfvZA_RNpEI8DyZN_qEXQZmx4QAAAAGilCGTAA")
STRING3 = getenv("STRING_SESSION3", "BQDF_T8AE3qJkEvDbivobqAJoTf1GMCz4niRImvF0U2_CPJbmA7EgJxNfEIx0MEkCt5wz4TMp8YdzU6u1GNYrDuIdycmpXcl81Xca001a6Z02CxhhqVJwGe0IZUiRCOjIDCH8Z8ENZJ_Sovpw0cw320ChEE2J9635Pvm3h6cox1PWDkvfl1KwtSkSu83nBmkh7YN3Pbz9kffmOJQ7W4314N88dT51AcUV-OPK3dtpy0KYSR6GXYwMS3UwdV8ucagfHXm2EpMgME6qVs1_Z6TScx4_YU9hq6qElq4ydkdcaTT73NlKXw4Pgn72OaEbMeuLSCQGfvZA_RNpEI8DyZN_qEXQZmx4QAAAAGilCGTAA")
STRING4 = getenv("STRING_SESSION4", "BQDF_T8AE3qJkEvDbivobqAJoTf1GMCz4niRImvF0U2_CPJbmA7EgJxNfEIx0MEkCt5wz4TMp8YdzU6u1GNYrDuIdycmpXcl81Xca001a6Z02CxhhqVJwGe0IZUiRCOjIDCH8Z8ENZJ_Sovpw0cw320ChEE2J9635Pvm3h6cox1PWDkvfl1KwtSkSu83nBmkh7YN3Pbz9kffmOJQ7W4314N88dT51AcUV-OPK3dtpy0KYSR6GXYwMS3UwdV8ucagfHXm2EpMgME6qVs1_Z6TScx4_YU9hq6qElq4ydkdcaTT73NlKXw4Pgn72OaEbMeuLSCQGfvZA_RNpEI8DyZN_qEXQZmx4QAAAAGilCGTAA")
STRING5 = getenv("STRING_SESSION5", "BQDF_T8AE3qJkEvDbivobqAJoTf1GMCz4niRImvF0U2_CPJbmA7EgJxNfEIx0MEkCt5wz4TMp8YdzU6u1GNYrDuIdycmpXcl81Xca001a6Z02CxhhqVJwGe0IZUiRCOjIDCH8Z8ENZJ_Sovpw0cw320ChEE2J9635Pvm3h6cox1PWDkvfl1KwtSkSu83nBmkh7YN3Pbz9kffmOJQ7W4314N88dT51AcUV-OPK3dtpy0KYSR6GXYwMS3UwdV8ucagfHXm2EpMgME6qVs1_Z6TScx4_YU9hq6qElq4ydkdcaTT73NlKXw4Pgn72OaEbMeuLSCQGfvZA_RNpEI8DyZN_qEXQZmx4QAAAAGilCGTAA")
STRING6 = getenv("STRING_SESSION6", "BQDF_T8AE3qJkEvDbivobqAJoTf1GMCz4niRImvF0U2_CPJbmA7EgJxNfEIx0MEkCt5wz4TMp8YdzU6u1GNYrDuIdycmpXcl81Xca001a6Z02CxhhqVJwGe0IZUiRCOjIDCH8Z8ENZJ_Sovpw0cw320ChEE2J9635Pvm3h6cox1PWDkvfl1KwtSkSu83nBmkh7YN3Pbz9kffmOJQ7W4314N88dT51AcUV-OPK3dtpy0KYSR6GXYwMS3UwdV8ucagfHXm2EpMgME6qVs1_Z6TScx4_YU9hq6qElq4ydkdcaTT73NlKXw4Pgn72OaEbMeuLSCQGfvZA_RNpEI8DyZN_qEXQZmx4QAAAAGilCGTAA")
STRING7 = getenv("STRING_SESSION7", "BQDF_T8AE3qJkEvDbivobqAJoTf1GMCz4niRImvF0U2_CPJbmA7EgJxNfEIx0MEkCt5wz4TMp8YdzU6u1GNYrDuIdycmpXcl81Xca001a6Z02CxhhqVJwGe0IZUiRCOjIDCH8Z8ENZJ_Sovpw0cw320ChEE2J9635Pvm3h6cox1PWDkvfl1KwtSkSu83nBmkh7YN3Pbz9kffmOJQ7W4314N88dT51AcUV-OPK3dtpy0KYSR6GXYwMS3UwdV8ucagfHXm2EpMgME6qVs1_Z6TScx4_YU9hq6qElq4ydkdcaTT73NlKXw4Pgn72OaEbMeuLSCQGfvZA_RNpEI8DyZN_qEXQZmx4QAAAAGilCGTAA")
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/7063e3b0eac98dcc5734e.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/35f71c3ebde68a5d7fc23.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/181715eb83d6b2dc4c1a1.jpg"
STATS_IMG_URL = "https://telegra.ph/file/3e8be4617f67d7369b44a.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/ed0b0c4bdba0e5edae53c.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/181715eb83d6b2dc4c1a1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/35f71c3ebde68a5d7fc23.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/7063e3b0eac98dcc5734e.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/181715eb83d6b2dc4c1a1.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/3e8be4617f67d7369b44a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/35f71c3ebde68a5d7fc23.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/3e8be4617f67d7369b44a.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
