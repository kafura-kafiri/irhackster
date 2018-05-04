from pymongo import MongoClient
from gridfs import GridFS
db_name = 'HACK'

client = MongoClient()
db = client[db_name]
fs = GridFS(client[db_name + '_FS'])

projects = db['projects']
