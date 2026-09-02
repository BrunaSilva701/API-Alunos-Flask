# importar o Flask
from flask import Flask, make_response,jsonify, request

# Importa o banco (bd.py)
from bd import Alunos

# criar uma instância do Flask
# __name__ assume o nome do arquivo que está sendo executado, neste caso main.py
app = Flask(__name__)

# Decorator - Marca a função com uma funcionalidade
# Rota que a função vai executar
@app.route('/alunos', methods=['GET'])
# Funções - Retorna os alunos usando o make_response e jsonify para retornar um JSON
def get_alunos():
    return make_response(jsonify(Alunos))

# Função - Buscar aluno pelo ID
@app.route('/alunos/<int:id>', methods=['GET'])
def get_alunosID(id):
    aluno = next((aluno for aluno in Alunos if aluno['id'] == id), None)

    if aluno is None:
        return make_response(jsonify({'Error: Aluno não encontrado'}))
    
    return make_response(jsonify(aluno))

# Função - Cria alunos e salva no bd.py
@app.route('/alunos', methods=['POST'])
def create_aluno():
    aluno = request.json
    Alunos.append(aluno)
    return make_response(jsonify(aluno))

# Função - Editar aluno pelo id
@app.route('/alunos/<int:id>', methods=['PUT'])
def edit_alunos(id):
    dados = request.json

    for aluno in Alunos:
        if aluno['id'] == id:
            aluno.update(dados)
            return make_response(jsonify(aluno))
        
    return make_response(jsonify({'Error: Aluno não encontrado'}))

# Função - Deletar aluno pelo id
@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_alunos(id):
    aluno = next((aluno for aluno in Alunos if aluno['id'] == id), None)

    if aluno is None:
        return make_response(jsonify({'Error: Aluno não encontrado'}))
    
    Alunos.remove(aluno)
    return make_response(jsonify(aluno))

# Permite que seja possivel acessar e iniciar
app.run()