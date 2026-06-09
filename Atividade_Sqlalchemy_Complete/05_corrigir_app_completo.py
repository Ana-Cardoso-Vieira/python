import os

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

pasta = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(pasta, "exercicio05.db")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()

        if nome and email:
            aluno = Aluno(nome=nome, email=email)
            db.session.add(aluno)
            db.session.commit()

        return redirect(url_for("index"))

    alunos = Aluno.query.order_by(Aluno.nome).all()
    return render_template("index.html", alunos=alunos)


@app.route("/editar/<int:aluno_id>", methods=["POST"])
def editar(aluno_id):
    aluno = db.session.get(Aluno, aluno_id)

    if aluno:
        aluno.nome = request.form.get("nome", "").strip()
        aluno.email = request.form.get("email", "").strip()
        db.session.commit()

    return redirect(url_for("index"))


@app.route("/excluir/<int:aluno_id>", methods=["POST"])
def excluir(aluno_id):
    aluno = db.session.get(Aluno, aluno_id)

    if aluno:
        db.session.delete(aluno)
        db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)