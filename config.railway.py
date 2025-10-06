import os

# Configuration pour Railway avec variables d'environnement

# The full URL base asset URL, with trailing slash.
ASSETS_BASEURL = '/assets/'

# The full URL base song URL, with trailing slash.
SONGS_BASEURL = '/songs/'

# Multiplayer websocket URL. Defaults to /p2 if blank.
MULTIPLAYER_URL = ''

# The email address to display in the "About Simulator" menu.
EMAIL = None

# Whether to use the user account system.
ACCOUNTS = True

# Custom JavaScript file to load with the simulator.
CUSTOM_JS = ''

# Default plugins to load with the simulator.
PLUGINS = [{
    'url': '',
    'start': False,
    'hide': False
}]

# Filetype to use for song previews. (mp3/ogg)
PREVIEW_TYPE = 'mp3'

# MongoDB server settings - Railway auto-injecte MONGO_URL
MONGO = {
    'host': [os.environ.get('MONGO_URL', '127.0.0.1:27017')],
    'database': 'taiko'
}

# Redis server settings - Railway auto-injecte REDIS_URL
REDIS = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379'),
}

# Secret key used for sessions.
SECRET_KEY = os.environ.get('SECRET_KEY', 'railway-secret-key-change-in-production')

# Git repository base URL.
URL = 'https://github.com/L3ne/taiko-web-master/'

# Google Drive API.
GOOGLE_CREDENTIALS = {
    'gdrive_enabled': False,
    'api_key': '',
    'oauth_client_id': '',
    'project_number': '',
    'min_level': None
}
