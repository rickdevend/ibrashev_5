from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Временное хранилище в памяти
users = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"}
}

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400

    new_id = max(users.keys(), default=0) + 1
    users[new_id] = {"id": new_id, "name": name}
    return jsonify(users[new_id]), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": f"User {user_id} deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    # Bandit обратит внимание на debug=True или host='0.0.0.0'
    app.run(host='0.0.0.0', port=5000, debug=True)