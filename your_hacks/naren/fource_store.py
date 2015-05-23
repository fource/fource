from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import logging,json

logger = logging.getLogger('fource')

hdlr = logging.FileHandler('/var/tmp/fource.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

hdlr.setFormatter(formatter)

logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)
	
class FourceStore(object):
	
	def __init__(self,host,port):

		#
		# Here database is fource_db and collection is fource_records
		#
		self.client = MongoClient(host,port)
		self.db = self.client.fource_db
		self.records = slef.db.fource_records

	def push_key(fource_key,value):
		try:
			insertion_id = self.records.insert({'_id':fource_key , 'data': json.dumps(value)})
			logger.info('successfully inserted key %s'%fource_key)
		except DuplicateKeyError:
			logger.error('duplicate key.Insertion not allowed')
		return insertion_id

	def pop_key(fource_key):
		self.records.remove({'_id':fource_key})
		logger.info('deleted %s successfully'%fource_key)
		return fource_key

	def peek_key(fource_key):
		results = json.laods(self.records.find_one({'_id':fource_key}))
		return results



"""
#Sample Usage

fource_client = FourceStore('localhost','27017')

#Add records
fource_client.push_key(key , {...})

#Remove from db
fource_client.pop_key(key)

#Fetch from db
fource_client.peek_key(key)

"""