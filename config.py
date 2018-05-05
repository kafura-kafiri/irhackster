from pymongo import MongoClient
from gridfs import GridFS
db_name = 'HACK'

client = MongoClient()
db = client[db_name]
fs = GridFS(client[db_name + '_FS'])

projects = db['projects']
users = db['USERS']

rooms = db['ROOMS']
messages = db['MESSAGES']

products = db['PRODUCTS']
