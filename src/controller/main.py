import requests, os, sys
from flask import Flask
from flask import request

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


from service.BicicletaController import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, validar_id

from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta
from service.TrancaService import listar_trancas


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

@app.route('/tranca', methods=['GET'])
def obter_trancas_route():
    # Resposta bem-sucedida (200 OK)
    trancas = listar_trancas()
    return trancas


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 4000)),host='0.0.0.0',debug=True)