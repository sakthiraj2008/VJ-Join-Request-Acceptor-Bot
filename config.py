from os import environ

API_ID = int(environ.get("API_ID", "11472991"))
API_HASH = environ.get("API_HASH", "c78c50d54baf2173e8b3f75c359c0c72")
BOT_TOKEN = environ.get("BOT_TOKEN", "7682114390:AAFPo30YL9Z-TsQphIYvWv9pVz-gHHtmnfA")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002318167392"))
ADMINS = int(environ.get("ADMINS", "-1002318167392"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "-1002318167392") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
