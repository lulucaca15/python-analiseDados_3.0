import pymongo

client_con = pymongo.MongoClient()
print(client_con.database_names())
db = client_con.cadastrodb
print(db.collection_names)
db.create_collection('mycollection')
print(db.collection_names())

db.mycollection.insert_one({
    'titulo' : 'Mongo DB com Python',
    'descricao' : 'MongoDB é um banco de dados NoSQL',
    'by' : 'datascienceacademy',
    'url' : 'http://www.datascienceacademy.com.br',
    'tags' : ['mongodb', 'database', 'NoSQL'],
    'likes' : 100    
})

print(db.mycollection.find_one())

doc1 = {
    'Nome' : 'Donald',
    'Sobrenome' : 'Trump',
    'Twitter' : '@POTUS'
}

db.mycollection.insert_one(doc1)

doc2 = {
    'Site' : 'http://www.datascienceacademy.com.br',
    'facebook' : 'facebook.com',
}

db.mycollection.insert_one(doc2)

for rec in db.mycollection.find():
    print(rec)

col = db['mycollection']
print(type(col))
print(col.count)

redoc = col.find_one()
print(redoc)


