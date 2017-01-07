import utils
from pymongo import MongoClient

config = utils.get_config()

#Mongo Connections 
dbConfig = config.get('mongo_users').get('db')
collectionConfig = config.get('mongo_users').get('collection')
user = config.get('mongo_users').get('user')
password = config.get('mongo_users').get('password')
client = MongoClient('mongodb://%s:%s@ds011291.mlab.com:11291/heroku_n940r2hr'%(user,password))
db= client[dbConfig]
collection = db[collectionConfig]
