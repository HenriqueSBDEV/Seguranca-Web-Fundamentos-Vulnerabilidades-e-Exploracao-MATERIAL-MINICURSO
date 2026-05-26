from flask import Flask, request

app = Flask(__name__)

users = {
    "1": "Carlos",
    "2": "Maria"
}

@app.route("/profile")
def profile():
    user_id = request.args.get("id")

    return f"Perfil de {users[user_id]}"