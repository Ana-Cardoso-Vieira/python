from flask import Flask, request, render_template_string

app = Flask(__name__)

usuarios = {
    "dolga": "cotemig2026",
    "janaina": "cotemig2026",
    "antonio": "cotemig2026",
    "ana clara": "22403230"
}

def mostrar_formulario():
    return render_template_string("""
        <h2>Login</h2>

        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>

            <input type="password" name="senha" placeholder="Senha"><br><br>

            <button type="submit">Entrar</button>
        </form>
    """)

def fazer_login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    for u, s in usuarios.items():
        if usuario == u and senha == s:
            return f"<h1>Bem-vindo, {usuario}!</h1>"

    return "<h1>Login inválido</h1>"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return fazer_login()
    else:
        return mostrar_formulario()

if __name__ == "__main__":
    app.run(debug=True)
    