# dumpmon.py
# Author: Jordan Wright
# Version: 0.0 (in dev)

# ---------------------------------------------------
# To Do:
#
#	- Refine Regex
#	- Create/Keep track of statistics

from lib.regexes import regexes
from lib.Pastebin import Pastebin, PastebinPaste
from lib.Slexy import Slexy, SlexyPaste
from lib.helper import log
from time import sleep
from settings import log_file
import argparse
import threading
import logging


def monitor():
    #while (True):
    #    print("running sleep permanently")
    #    sleep(20)
    #return 0;
    '''
    monitor() - Main function... creates and starts threads

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", help="more verbose", action="store_true")
    args = parser.parse_args()

    # Configure logging
    level = logging.INFO
    if args.verbose:
        level = logging.DEBUG
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s', filename=log_file, level=level)
    logging.info('Monitoring...')


    # Create lock for both output log 
    log_lock = threading.Lock()
    tweet_lock = threading.Lock() # TODO: should be removed to simplify to simplify

    pastebin_thread = threading.Thread(
        target=Pastebin().monitor, args=[tweet_lock])
    slexy_thread = threading.Thread(
        target=Slexy().monitor, args=[tweet_lock])

    for thread in (pastebin_thread, slexy_thread):
        thread.daemon = True
        thread.start()

    # Let threads run
    try:
        while(1):
            sleep(5)
    except KeyboardInterrupt:
        logging.warn('Stopped.')


if __name__ == "__main__":
    monitor()
