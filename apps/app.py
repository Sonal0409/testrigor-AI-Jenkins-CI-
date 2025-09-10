from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Python app!"})

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    return jsonify({
        "id": 1,
        "name": data["name"],
        "createdAt": "2025-09-10"
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
