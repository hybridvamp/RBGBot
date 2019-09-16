import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("692016120:AAGVshlfLDOovACCdvyI7ZHPxTQ5xQ_dCpA", None)
    # required for running on Heroku
    URL = os.environ.get("https://git.heroku.com/rbgbot.git", "")
    PORT = int(os.environ.get("PORT", 5000))
    # get a token from ChatBase.com for analytics
    CBTOKEN = os.environ.get('CBTOKEN', None)
    # Python3 ReQuests CHUNK SIZE
    CHUNK_SIZE = 10281
    # ReMove.BG API Key
    REM_BG_API_KEY = os.environ.get("RhiWqnF93rppJ7smerzFqJFRR", None)
    # temporary download location
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS")
