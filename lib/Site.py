from Queue import Queue
import requests
import time
import re
from requests import ConnectionError
from settings import DB_HOST, DB_PORT, DB_DB, DB_PWD, DB_USER
import mysql.connector
import logging
import helper


class Site(object):
    '''
    Site - parent class used for a generic
    'Queue' structure with a few helper methods
    and features. Implements the following methods:

            empty() - Is the Queue empty
            get(): Get the next item in the queue
            put(item): Puts an item in the queue
            tail(): Shows the last item in the queue
            peek(): Shows the next item in the queue
            length(): Returns the length of the queue
            clear(): Clears the queue
            list(): Lists the contents of the Queue
            download(url): Returns the content from the URL

    '''
    # I would have used the built-in queue, but there is no support for a peek() method
    # that I could find... So, I decided to implement my own queue with a few
    # changes
    def __init__(self, queue=None):
        if queue is None:
            self.queue = []

        print("CONNECTING", DB_HOST, DB_PORT)
        self.mysql_client = mysql.connector.connect(
          host=DB_HOST,
          user=DB_USER,
          password=DB_PWD,
          database=DB_DB
        )


    def empty(self):
        return len(self.queue) == 0

    def get(self):
        if not self.empty():
            result = self.queue[0]
            del self.queue[0]
        else:
            result = None
        return result

    def put(self, item):
        self.queue.append(item)

    def peek(self):
        return self.queue[0] if not self.empty() else None

    def tail(self):
        return self.queue[-1] if not self.empty() else None

    def length(self):
        return len(self.queue)

    def clear(self):
        self.queue = []

    def list(self):
        print("QUEUE: ", self.BASE_URL)
        print('\n'.join(url for url in self.queue))

    def monitor(self, t_lock):
        self.update()
        while(1):
            self.list()
            while not self.empty():
                paste = self.get()
                self.ref_id = paste.id
                logging.info('[*] Checking ' + paste.url)
                paste.text = self.get_paste_text(paste)
                tweet = helper.build_tweet(paste)
                print("trying to insert: ", paste.id)
                with t_lock:
                    print("INSERTING INTO db", paste.id)
                    db_cursor = self.mysql_client.cursor()
                    query_add_record = ("INSERT INTO pastes VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);")
                    query_data = ( ""+paste.id, ""+paste.text, ""+paste.emails, ""+paste.hashes, ""+paste.num_emails, ""+paste.num_hashes, ""+paste.type, ""+paste.db_keywords, ""+paste.url)

                    db_cursor.execute(query_add_record, query_data)

                    client.commit()
                    cursor.close()

            time.sleep(30) # sleep 30 seconds before every message monitor
            self.update()
            while self.empty():
                logging.debug('[*] No results... sleeping')
                time.sleep(self.sleep)
                self.update()
