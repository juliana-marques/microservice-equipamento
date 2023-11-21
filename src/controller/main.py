import os, sys
from flask import Flask,  request
from unittest.mock import Mock

app = Flask(__name__)
requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)                                                                 

from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, validar_id, deletar_bicicleta
from service.TotemService import listar_totens, cadastrar_totem, editar_totem, validar_id_totem, deletar_totem
from service.TrancaService import listar_trancas, cadastrar_tranca, buscar_tranca_por_id, editar_tranca, deletar_tranca, obter_bicicleta_tranca

###### config do SONAR do problema de CSRF ###### 
from flask_wtf import CSRFProtect               #
from flask_wtf.csrf import generate_csrf        #
                                                #
csrf = CSRFProtect(app)                         #
csrf.init_app(app)                              #
app.config['SECRET_KEY'] = 'teste123'           #
                                                #
@app.route('/get_csrf_token', methods=['GET'])  #
def get_csrf_token():                           #
    token = generate_csrf()                     #
    return token, 200                           #
#################################################

bicicletas = []

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World! :)"


@app.route('/bicicleta', methods=['GET'])
def listar_bicicletas_route():
    return listar_bicicletas()


@app.route('/bicicleta', methods=['POST'])
def cadastrar_bicicleta_route():
    bicicleta = request.json
    
    cadastrar_bicicleta(bicicleta)
    response_mock = Mock()
    response_mock.status_code = "Dados atualizados", 200
    response_mock.json.return_value = request.json
    return response_mock.json()

@app.route('/bicicleta/<int:bicicleta_id>', methods=['PUT'])
def editar_bicicleta_route(bicicleta_id):
    bicicleta = request.json

    bike_new = editar_bicicleta(bicicleta_id, bicicleta)
    response_mock = Mock()
    response_mock.status_code = "Dados atualizados", 200
    response_mock.json.return_value = bike_new
    return bike_new

@app.route('/bicicleta/<int:bicicleta_id>', methods=['DELETE'])
def deletar_bicicleta_route(bicicleta_id):
    isDelete = deletar_bicicleta(bicicleta_id)
    response_mock = Mock()
    if isDelete == True:
        response_mock.status_code = 200
        response_mock.json.return_value = "Dados removidos"
    
    if isDelete == False:
        response_mock.status_code = 404
        response_mock.json.return_value = "Dados não encontrados"

    return response_mock.json()

@app.route('/totem', methods=['GET'])
def listar_totens_route():
    return listar_totens()


@app.route('/totem', methods=['POST'])
def cadastrar_totem_route():
    data = request.json
    totem = Totem(data.get('localizacao'), data.get('descricao'))
    response_mock = Mock()
    response_mock.status_code = "Dados cadastrados", 200
    response_mock.json_return_value = cadastrar_totem(totem)

    return response_mock.json()


@app.route('/totem/<int:id_totem>', methods=['PUT'])
def editar_totem_route(id_totem):

    data = request.json
    totem = Totem(data.get('localizacao'), data.get('descricao'))
    response_mock = Mock()
    response_mock.status_code = "Dados atualizados", 200
    response_mock.json.return_value =  editar_totem(id_totem, totem)

    return response_mock.json()


@app.route('/totem/<int:id_totem>', methods=['DELETE'])
def deletar_totem_route(id_totem):
    return deletar_totem(id_totem)
    

@app.route('/tranca', methods=['GET'])
def obter_trancas_route():
    return listar_trancas()


@app.route('/tranca', methods=['POST'])
def cadastrar_trancas_route():
    data = request.json
    numero, localizacao, ano_de_fabricacao, modelo, status = data.get('numero'), data.get('localizacao'), data.get('ano_de_fabricacao'), data.get('modelo'), data.get('status')

    return cadastrar_tranca(numero, localizacao, ano_de_fabricacao, modelo, status)


@app.route('/tranca/<int:id_tranca>', methods=['GET'])
def obter_tranca_por_id_route(id_tranca):
    return buscar_tranca_por_id(id_tranca)


@app.route('/tranca/<int:id_tranca>', methods=['PUT'])
def editar_tranca_rout(id_tranca):
    data = request.json
    numero, localizacao, ano_de_fabricacao, modelo, status = data.get('numero'), data.get('localizacao'), data.get('ano_de_fabricacao'), data.get('modelo'), data.get('status')

    return editar_tranca(id_tranca, numero, localizacao, ano_de_fabricacao, modelo, status)


@app.route('/tranca/<int:id_tranca>', methods=['DELETE'])
def deletar_tranca_route(id_tranca):
    return deletar_tranca(id_tranca)

@app.route('/tranca/<int:id_tranca>/bicicleta', methods=['GET'])
def obter_bicicleta_por_tranca(id_tranca):
    bicicleta = obter_bicicleta_tranca(id_tranca)


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
