## DOCUMENTAÇÃO
[Flask](https://flask.palletsprojects.com/en/stable/)

[Python](https://docs.python.org/3/using/windows.html)

## PASSO A PASSO
1. Baixar o Python
1. Cria o ambiente virtual ``python -m venv .venv``
2. Ativa o ambiente virtual ``.venv\Scripts\activate``
3. Cria arquivo principal do projeto ``main.py``
4. Instala o Flask ``pip install Flask``

## INTERAÇÃO COM O TERMINAL
1. Escreve ``python`` para iniciar a interação
2. Escreve ``exit()`` para sair

## EXEMPLO
`````
from flask import Flask, jsonify

app = Flask(__name__)

# Dados de exemplo simulando um banco de dados
cursos = [
    {"id": 1, "nome": "Python para Iniciantes"},
    {"id": 2, "nome": "Desenvolvimento Web com Flask"}
]

@app.route('/cursos', methods=['GET'])
def obter_cursos():
    return jsonify(cursos)

if __name__ == '__main__':
    app.run(debug=True)
````