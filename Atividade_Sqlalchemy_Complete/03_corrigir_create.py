from corrigir_models import db, Aluno
def cadastrar_aluno(nome, email):
    """CREATE - insere um aluno no banco."""

    aluno = Aluno(nome=nome, email=email)

    db.session.add(aluno)
    db.session.commit()

    return aluno