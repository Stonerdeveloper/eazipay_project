# eazipay_project
Service 1: GraphQL Service Documentation
Service Overview
Name: fastApiProject

Description: This service provides a GraphQL API for querying user data.

Endpoints
GraphQL Endpoint: /graphql
Description: Accepts GraphQL queries for retrieving user data.
Method: POST
Example Query:
graphql
Copy code
{
    user(id: "123") {
        id
        name
        email
    }
}
GraphQL Schema
User Type

Fields:
id (ID): Unique identifier for the user.
name (String): User's name.
email (String): User's email address.
Queries

user(id: ID!): Retrieve a user by their ID.
Error Handling
HTTP Status Codes:
200 OK: Successful request.
400 Bad Request: Invalid GraphQL query.
500 Internal Server Error: Internal server error.
Dependencies
FastAPI: Python web framework for building GraphQL API.
Ariadne: GraphQL toolkit for Python.
Uvicorn: ASGI server for running the FastAPI application.
Requests: HTTP library for making requests to Service 2.



Service 2: MongoDB Service Documentation
Service Overview
Name: flaskProject1

Description: This service manages a MongoDB database that stores user data.

Endpoints
User Data Endpoint: /get_user/<user_id>
Description: Retrieve user data from the MongoDB database.
Method: GET
URL Parameter:
user_id (String): The unique identifier of the user.
Database Schema
Collection Name: users
Fields:
_id (ObjectId): MongoDB's automatically generated unique identifier.
name (String): User's name.
email (String): User's email address.
Error Handling
HTTP Status Codes:
200 OK: Successful request.
404 Not Found: User not found in the database.
500 Internal Server Error: Internal server error.
Dependencies
Flask: Python web framework for creating the MongoDB service.
PyMongo: MongoDB driver for Python for database operations.
MongoDB Atlas: Cloud-based MongoDB database service.
Integration
Service 1 (GraphQL Service) makes HTTP requests to Service 2 (MongoDB Service) to retrieve user data.
Ensure both services are running and accessible for integration.
Authentication and Security
Implement proper authentication mechanisms for both services.
Use environment variables or secure configuration files for sensitive data (e.g., MongoDB URI and API keys).
