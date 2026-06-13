from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {
    "admin": "admin123",
}
TRANSACTIONS = {}

@app.route("/auth", methods=["POST"])
def auth():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if USERS.get(username) == password:
        return jsonify({
            "status": "success",
            "message": "Authenticated",
        })
    return jsonify({
        "status": "failed",
        "message": "Incorrect username or password",
    }), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)