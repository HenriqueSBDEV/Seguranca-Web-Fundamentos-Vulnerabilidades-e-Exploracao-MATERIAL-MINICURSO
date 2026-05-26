from flask import Flask, request

app = Flask(__name__)

users = {
    "1": "Carlos",
    "2": "Maria"
}

logged_user_id = "1"

@app.route("/profile")
def profile():
    user_id = request.args.get("id")

    if user_id != logged_user_id:
        return "Acesso negado"

    return f"Perfil de {users[user_id]}"