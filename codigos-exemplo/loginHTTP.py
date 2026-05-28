from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():

    return """

    <h1>Login HTTP Vulnerável</h1>

    <form action="/login" method="POST">

        <input type="text"
               name="username"
               placeholder="Usuário">

        <br><br>

        <input type="password"
               name="password"
               placeholder="Senha">

        <br><br>

        <button type="submit">
            Entrar
        </button>

    </form>
    """

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    return f"""
    <h1>Login realizado</h1>

    Usuário: {username}<br>
    Senha: {password}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)