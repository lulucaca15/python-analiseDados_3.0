from pymongo import MongoClient
import datetime

conn = MongoClient('localhost', 27017)

print(type(conn))

db = conn.cadastrodb
print(type(db))

collection = db.cadastrodb
print(type(collection))

post1 = {
    'codigo' : 'ID-9987725',
    'prod_name' : 'Geladeira',
    'marcas' : ['brastemp', 'consul', 'electrolux'],
    'data_cadastro' : datetime.datetime.utcnow()
} 
print(type(post1))

collection = db.posts
post_id = collection.insert_one(post1)
post_id.inserted_id
post_id

post2 = {
    'codigo' : 'ID-2209846',
    'prod_name' : 'Televisao',
    'marcas' : ['samsung', 'lg', 'panasonic'],
    'data_cadastro' : datetime.datetime.utcnow()
} 
collection = db.posts
post_id = collection.insert_one(post2).inserted_id
post_id

print(collection.find_one({"prod_name" : "Televisao"}))

for post in collection.find():
      print(post)
      
print (db.name)
print(db.collection_names)