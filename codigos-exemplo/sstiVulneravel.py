from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():

    nome = request.args.get("nome")

    template = f"""
    <h1>Olá {nome}</h1>
    """

    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)