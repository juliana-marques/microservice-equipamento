import requests, os, sys
from flask import Flask
from flask import request

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, validar_id, deletar_bicicleta
from service.TotemService import listar_totens, cadastrar_totem, editar_totem, validar_id_totem, deletar_totem
from service.TrancaService import listar_trancas, cadastrar_tranca


app = Flask(__name__)

@app.route('/bicicleta', methods=['GET'])
def listar_bicicletas_route():
    bicicletas = listar_bicicletas()
    return bicicletas


@app.route('/bicicleta', methods=['POST'])
def cadastrar_bicicleta_route():
    data = request.form

    marca = data.get('marca')
    modelo = data.get('modelo')
    ano = data.get('ano')
    numero = data.get('numero')
    status = data.get('status')

    response = cadastrar_bicicleta(marca, modelo, ano, numero, status)

    return response

@app.route('/bicicleta/<int:bicicleta_id>', methods=['PUT'])
def editar_bicicleta_route(bicicleta_id):

    verificacao = validar_id(bicicleta_id)

    if verificacao != True:
        return verificacao

    data = request.form

    marca = data.get('marca')
    modelo = data.get('modelo')
    ano = data.get('ano')
    numero = data.get('numero')
    status = data.get('status')

    response = editar_bicicleta(bicicleta_id, marca, modelo, ano, numero, status)

    return response

@app.route('/bicicleta/<int:bicicleta_id>', methods=['DELETE'])
def deletar_bicicleta_route(bicicleta_id):

    response = deletar_bicicleta(bicicleta_id)
    return response

@app.route('/totem', methods=['GET'])
def listar_totens_route():
    totens = listar_totens()
    return totens

@app.route('/totem', methods=['POST'])
def cadastrar_totem_route():
    data = request.form

    localizacao = data.get('localizacao')
    descricao = data.get('descricao')

    response = cadastrar_totem(localizacao, descricao)

    return response

@app.route('/totem/<int:idTotem>', methods=['PUT'])
def editar_totem_route(idTotem):

    verificacao = validar_id_totem(idTotem)

    if verificacao != True:
        return verificacao

    data = request.form

    localizacao = data.get('localizacao')
    descricao = data.get('descricao')

    response = editar_totem(idTotem,localizacao, descricao)

    return response

@app.route('/totem/<int:idTotem>', methods=['DELETE'])
def deletar_totem_route(idTotem):

    response = deletar_totem(idTotem)
    return response

@app.route('/tranca', methods=['GET'])
def obter_trancas_route():
    # Resposta bem-sucedida (200 OK)
    trancas = listar_trancas()
    return trancas

@app.route('/tranca', methods=['POST'])
def cadastrar_trancas_route():
    data = request.get_json()

    numero = data.get('numero')
    localizacao = data.get('localizacao')
    anoDeFabricacao = data.get('anoDeFabricacao')
    modelo = data.get('modelo')
    status = data.get('status')

    response = cadastrar_tranca(numero, localizacao, anoDeFabricacao, modelo, status)

    return response

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 4000)),host='0.0.0.0',debug=True)