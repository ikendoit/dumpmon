# settings.py
import os

DB_HOST = "mysql_db"
DB_PORT = 3306
DB_PWD = '123456'
DB_DB = 'pastes_db'
DB_USER = 'user'

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
