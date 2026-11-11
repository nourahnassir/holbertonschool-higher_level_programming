#!/usr/bin/python3
"""
Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """Status endpoint returning OK."""
    return "OK"


@app.route('/data')
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """Returns the full object corresponding to the provided username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the users dictionary via POST request."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    response_data = {
        "message": "User added",
        "user": data
    }
    return jsonify(response_data), 201


if __name__ == "__main__":
    app.run()
