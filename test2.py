import pymongo

client = pymongo.MongoClient("mongodb+srv://root1:1234@cluster0.l5frp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
d = {
    "name":"deepak",
    "email":"deepak@ineuron.ai",
    "surname":"kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
