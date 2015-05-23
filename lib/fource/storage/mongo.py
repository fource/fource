from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import logging,json

logger = logging.getLogger('fource')
hdlr = logging.FileHandler('/tmp/fource.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


class MongoStore(object):
    """
    Store and retrive check results from mongo
    """

    def __init__(self, host, port):
        """
        Here database name is fource and collection is records
        """
        self.client = MongoClient(host, port)
        self.db = self.client.fource
        self.records = self.db.records

    def save(self, key, data):
        try:
            insertion_id = self.records.update(
                {'_id': key},
                {'$set': {'data': data}},
                True,
            )
            logger.info('successfully inserted key %s' % key)
        except DuplicateKeyError as e:
            logger.error('duplicate key.Insertion not allowed. Message: %s'
                         % e.message)
        return insertion_id


    def get(self, key):
        results = self.records.find_one({'_id': key})
        if results and results.get('data'):
            return results.get('data')
        else:
            return {}

    def delete(self, key):
        self.records.remove({'_id': key})
        logger.info('deleted %s successfully' % key)
        return key
