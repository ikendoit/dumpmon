'''
helper.py - provides misc. helper functions
Author: Jordan

'''

import requests
import settings
from time import sleep, strftime
import logging
from tenacity import *


r = requests.Session()


# tenacity api
@retry(stop=stop_after_attempt(3), wait=wait_fixed(5) + wait_random(0, 2))
def download(url, headers=None):
    if not headers:
        headers = None
    if headers:
        r.headers.update(headers)

    log("downloading: " + url )
    sleep(4)
    response = r.get(url).text
    log("got response from " + url)

    return response


def log(text, log_method='info'):
    '''
    log(text): Logs message to both STDOUT and to .output_log file

    '''

    # doing logging[log_method] throws "has no attribute __getitem__" exception
    getattr(logging,log_method)(text)
    with open(settings.log_file, 'a') as logfile:
        logfile.write(str(text) + '\n')


def build_tweet(paste):
    '''
    build_tweet(url, paste) - Determines if the paste is interesting and, if so, builds and returns the tweet accordingly

    '''
    tweet = None
    if paste.match():
        tweet = paste.url
        if paste.type == 'db_dump':
            if paste.num_emails > 0:
                tweet += ' Emails: ' + str(paste.num_emails)
            if paste.num_hashes > 0:
                tweet += ' Hashes: ' + str(paste.num_hashes)
            if paste.num_hashes > 0 and paste.num_emails > 0:
                tweet += ' E/H: ' + str(round(
                    paste.num_emails / float(paste.num_hashes), 2))
            tweet += ' Keywords: ' + str(paste.db_keywords)
        elif paste.type == 'google_api':
            tweet += ' Found possible Google API key(s)'
        elif paste.type in ['cisco', 'juniper']:
            tweet += ' Possible ' + paste.type + ' configuration'
        elif paste.type == 'ssh_private':
            tweet += ' Possible SSH private key'
        elif paste.type == 'honeypot':
            tweet += ' Dionaea Honeypot Log'
        elif paste.type == 'pgp_private':
            tweet += ' Found possible PGP Private Key'
        tweet += ' #infoleak'
    if paste.num_emails > 0:
        print(paste.emails)
    return tweet
