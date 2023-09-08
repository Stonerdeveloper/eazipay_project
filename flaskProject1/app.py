from flask import Flask, jsonify
import pymongo

app = Flask(__name__)

# MongoDB configuration
mongo_uri = "mongodb+srv://echetaldikechukwuemeka:Td4IISAHNZZHOghQ@cluster0.7dcmamg.mongodb.net/?retryWrites=true&w=majority" 
client = pymongo.MongoClient(mongo_uri)

db = client["dbname"]
collection = db["users"]

@app.route("/get_user/<user_id>", methods=["GET"])
def get_user(user_id):
    # Simulate fetching user data from MongoDB
    user_data = collection.find_one({"_id": user_id})
    return jsonify(user_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
