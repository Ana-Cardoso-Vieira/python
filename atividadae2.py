from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Ana Clara Cardoso Vieira </li>  
                <li><strong>Email:</strong> anaclaracardoso8868@gmail.com </li>
                <li><strong>Telefone:</strong> (31) 972612171</li>
            </ul>

            
            <h2>Formação Acadêmica</h2>
            <ul>
                <li><strong>Colégio:</strong> Cotemig cursando: 3° Ano Ensino Médio </li>  
           
            </ul>

            <h2>Experiência Profissional</h2>
            <ul>
                <li><strong>Empresa:</strong> 1001 Festas </li>
                <li><strong>Cargo:</strong> Auxiliar de Loja</li>
                <li><strong>Período:</strong> Jun 2023 - Concluido</li>
            </ul>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)