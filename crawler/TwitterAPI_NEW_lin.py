import twitter
import urlparse # python 2.7
# import urllib # python 3.0
import logging
import time
from datetime import datetime
from PersistingIO_lin import *
import sys

class TwitterAPI(object):
    """
    TwitterAPI class allows the Connection to Twitter via OAuth
    once you have registered with Twitter and receive the 
    necessary credentials 
    """
    def __init__(self): 
        consumer_key = 'zuYVausrnNtJyg63jOuJ5yBPq'
        consumer_secret = 'n2emCbH40fHAkDkPiVQZp9NxWrWyalFEvEaxsCVJjPpmzzdlus'
        access_token = '709701888946470913-e1QB1VLWJX4r86qNzRTjT4Xhdf6OtnI'
        access_secret = 'ZX8jMhHkhr0frEoTS1h8rdcmLRPjjQSzBU29X9sna3Wu4'
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.retries = 3
        self.auth = twitter.oauth.OAuth(access_token, access_secret, consumer_key, consumer_secret)
        self.api = twitter.Twitter(auth=self.auth)
        
        # logger initialisation
        appName = 'AlexBigSmall'
        self.logger = logging.getLogger(appName)
        #self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        logPath = 'data'
        fileName = appName
        fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler) 
        self.logger.setLevel(logging.DEBUG)
        
        # Save to JSON file initialisation
        jsonFpath = 'data'
        jsonFname = 'result2'
        self.jsonSaver = IO_json(jsonFpath, jsonFname)
        
        # Save to MongoDB Intitialisation
        self.mongoSaver = IO_mongo(db='twtr01_db', coll='twtr01_coll')

    def searchTwitter(self, q, max_res=1000, **kwargs):
        search_results = self.api.search.tweets(q=q, count=max_res, **kwargs)
        statuses = search_results['statuses']
        max_results = min(1000, max_res) 
        
        while True:
            try:
                next_results = search_results['search_metadata']['next_results']
                # self.logger.info('info in searchTwitter - next_results:%s'% next_results[1:])
            except KeyError as e:
            	#self.logger.error('error in searchTwitter: %s', %(e))
                break
            
            next_results = urlparse.parse_qsl(next_results[1:]) # python 2.7
            # next_results = urllib.parse.parse_qsl(next_results[1:])
            # self.logger.info('info in searchTwitter - next_results[max_id]:', next_results[0:])

            kwargs = dict(next_results)
            log_str = 'info in searchTwitter - next_results[max_id]:%s'% kwargs['max_id']
            print log_str
            self.logger.info(log_str)
            print 'searching Tweets'
            search_results = self.api.search.tweets(**kwargs)
            statuses += search_results['statuses']
            self.saveTweets(search_results['statuses'])
            # if len(statuses) > max_results:
            #     self.logger.info('info in searchTwitter - got %i tweets - max: %i' %(len(statuses), max_results))
            #     break
        # return statuses

    def saveTweets(self, statuses):
        print 'save to json'
        # Saving to JSON File
        self.jsonSaver.save(statuses)
        
        # Saving to MongoDB
        for s in statuses:
            self.mongoSaver.save(s)

    def parseTweets(self, statuses):
        print 'parse Tweets'
        return [ (status['id'], 
                  status['created_at'], 
                  status['user']['id'],
                  status['user']['name'], 
                  status['text'], 
                  url['expanded_url']) 
                        for status in statuses 
                            for url in status['entities']['urls'] ]

    def getTweets(self, q,  max_res=10):
        """
        Make a Twitter API call whilst managing rate limit and errors.
        """
        def handleError(e, wait_period=2, sleep_when_rate_limited=True):

            if wait_period > 3600: # Seconds
                #self.logger.error('Too many retries in getTweets: %s', %(e))
                raise e
            if e.e.code == 401:
                #self.logger.error('error 401 * Not Authorised * in getTweets: %s', %(e))
                return None
            elif e.e.code == 404:
                #self.logger.error('error 404 * Not Found * in getTweets: %s', %(e))
                return None
            elif e.e.code == 429: 
                #self.logger.error('error 429 * API Rate Limit Exceeded * in getTweets: %s', %(e))
                if sleep_when_rate_limited:
                    self.logger.error('error 429 * Retrying in 15 minutes * in getTweets: %s')
                    sys.stderr.flush()
                    time.sleep(60*15 + 5)
                    # self.logger.info('error 429 * Retrying now * in getTweets: %s', %(e))
                    return 2
                else:
                    raise e # Caller must handle the rate limiting issue
            elif e.e.code in (500, 502, 503, 504):
                self.logger.info('Encountered %i Error. Retrying in %i seconds' % (e.e.code, wait_period))
                time.sleep(wait_period)
                wait_period *= 1.5
                return wait_period
            else:
                #self.logger.error('Exit - aborting - %s', %(e))
                raise e
        
        while True:
            wait_period = 2
            try:
                self.searchTwitter( q, max_res=1000)
            except twitter.api.TwitterHTTPError as e:
                print 'Error occurred'
                print e

                error_count = 0 
                wait_period = handleError(e, wait_period)
                # if wait_period is None:
                #     return

t=TwitterAPI()
q="#RobinWilliams"
tsearch=t.getTweets(q)
pp(tsearch[1])