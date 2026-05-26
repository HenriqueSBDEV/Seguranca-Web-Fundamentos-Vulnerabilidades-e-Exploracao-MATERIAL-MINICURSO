from flask import Flask, request

app = Flask(__name__)

email = "user@email.com"

@app.route("/")
def home():
    return f"""
    <h1>Painel</h1>

    <p>Email atual: {email}</p>

    <form action="/change-email" method="POST">
        <input type="email" name="new_email">
        <button>Alterar</button>
    </form>
    """

@app.route("/change-email", methods=["POST"])
def change():
    global email
    email = request.form["new_email"]
    return "Email alterado"

app.run(debug=True)