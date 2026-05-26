from flask import Flask, request, session
import secrets

app = Flask(__name__)

app.secret_key = "segredo"

email = "user@email.com"

@app.route("/")
def home():

    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)

    return f"""

    <h1>Painel do Usuário</h1>

    <p>Email atual: {email}</p>

    <form action="/change-email" method="POST">

        <input 
            type="hidden"
            name="csrf_token"
            value="{session['csrf_token']}"
        >

        <input type="email" name="new_email">

        <button type="submit">
            Alterar Email
        </button>

    </form>
    """

@app.route("/change-email", methods=["POST"])
def change_email():

    global email

    token = request.form.get("csrf_token")

    if token != session["csrf_token"]:
        return "CSRF detectado"

    email = request.form.get("new_email")

    return f"Email alterado para: {email}"

if __name__ == "__main__":
    app.run(debug=True)