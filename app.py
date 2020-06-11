from pymongo import MongoClient


# Config
MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)

db = client['pymongo']
collection = db['products']

# Insert one
collection.insert_one({"name": "tablet", "price": 600})

# Insert many
product_one = {"name": "mouse", "price": 100}
product_two = {"name": "monitor", "price": 600}

r = collection.insert_many([product_one, product_two])
print(r.__str__())

# Get all
data = collection.find()
for i in data:
    print(i)

data = collection.find({"price": 600})
for i in data:
    print(i)

# Get one
print(collection.find_one({
    "price": 300
}))

# Delete many
collection.delete_many({"price": 600})

# Delete one
collection.delete_one({"name": "tablet"})

# Update one
collection.update_one({
    "name": "tablet"
}, {
    "$set": {
        "name": "Ipad",
        "price": 800
    }
})

# Count
print(collection.count_documents({}))

# Delete all
collection.delete_many({})