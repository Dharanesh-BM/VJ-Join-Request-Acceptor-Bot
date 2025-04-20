from os import environ

API_ID = int(environ.get("API_ID", "7402029"))
API_HASH = environ.get("API_HASH", "846ffd84bacc021587353f132583306e")
BOT_TOKEN = environ.get("BOT_TOKEN", "7911923199:AAE5zEIEtuIfrETMTfHifaw7kwm61rRlr44")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002529775878"))
ADMINS = int(environ.get("ADMINS", "827181010"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://mrlocal2345:CkD2NxCCoIaXHeyb@cluster0.jsb4jkv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
