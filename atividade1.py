from flask import Flask

app = Flask(__name__)

@app.route("/decorator")
def decorator():
    return """
    <h1>Decorator em Python</h1>

    <p>
    Decorator adiciona funções extras a outra função.
    </p>

    <p>
    No Flask, @app.route() cria rotas.
    </p>
    
    """

if __name__ == "__main__":
    app.run(debug=True)