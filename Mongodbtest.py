import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"biki",
    "email":"raaj777@gmail.com",
    "surname":"kumar"

}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
