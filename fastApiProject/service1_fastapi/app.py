from fastapi import FastAPI
import requests
from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL
import uvicorn

app = FastAPI()

# MongoDB configuration
mongo_uri = "mongodb+srv://echetaldikechukwuemeka:Td4IISAHNZZHOghQ@cluster0.7dcmamg.mongodb.net/?retryWrites=true&w=majority" 
client = pymongo.MongoClient(mongo_uri)

db = client["graphql_definitions"]  # Create or use an existing database
definitions_collection = db["definitions"]  # Create a collection to store definitions

# GraphQL schema setup
query = QueryType()
user = ObjectType("User")

type_defs = gql("""
    type Query {
        user(id: ID!): User
    }
    type User {
        id: ID!
        name: String
        email: String
    }
""")

schema = make_executable_schema(type_defs, query, user)

@query.field("user")
def resolve_user(_, info, id):
    # Make an HTTP request to Service 2 to fetch user data
    service2_url = "http://localhost:8080/get_user/" + id
    response = requests.get(service2_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
