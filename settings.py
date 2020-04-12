# settings.py
import os

USE_DB = True
DB_HOST = os.environ.get('DB_1_PORT_27017_TCP_ADDR') # service name "db" is defined in docker-compose file
DB_PORT = 27017

# Twitter Settings
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Thresholds
EMAIL_THRESHOLD = 20
HASH_THRESHOLD = 30
DB_KEYWORDS_THRESHOLD = .55

# Time to Sleep for each site
SLEEP_SLEXY = 60
SLEEP_PASTEBIN = 15
SLEEP_PASTIE = 30

# Other configuration
tweet_history = "tweet.history"
log_file = "output.log"
