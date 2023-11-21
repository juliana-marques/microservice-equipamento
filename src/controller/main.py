import os, sys
from flask import Flask,  request
from unittest.mock import Mock

app = Flask(__name__)
requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)                                                                 

from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, deletar_bicicleta, listar_bicicleta_id, integrar_bicicleta_rede, retirar_bicicleta_rede
from service.TotemService import listar_totens, cadastrar_totem, editar_totem, deletar_totem, listar_totem_id
from service.TrancaService import listar_trancas, cadastrar_tranca, editar_tranca, deletar_tranca, listar_tranca_id, integrar_tranca_rede, retirar_tranca_rede, validar_tranca_integrar_bicicleta, fechamento_da_tranca, validar_tranca_retirar_bicicleta

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
dados_cadastrados = "Dados cadastrados"
dados_atualizados = "Dados atualizados"
dados_removidos = "Dados removidos"
dados_nao_encontrados = "Dados não encontrados"
dados_invalidos = "Dados inválidos"

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/bicicleta', methods=['GET'])
def listar_bicicletas_route():
    return listar_bicicletas()


@app.route('/bicicleta/<int:bicicleta_id>', methods=['GET'])
def listar_bicicleta_id_route(bicicleta_id):
    return listar_bicicleta_id(bicicleta_id)


@app.route('/bicicleta', methods=['POST'])
def cadastrar_bicicleta_route():
    bicicleta = request.json
    
    cadastrar_bicicleta(bicicleta)
    response_mock = Mock()
    response_mock.status_code = dados_cadastrados, 200
    response_mock.json.return_value = request.json, 200
    return response_mock.json()

@app.route('/bicicleta/<int:bicicleta_id>', methods=['PUT'])
def editar_bicicleta_route(bicicleta_id):
    bicicleta = request.json

    bike_new = editar_bicicleta(bicicleta_id, bicicleta)
    response_mock = Mock()
    response_mock.status_code = "Dados atualizados", 200
    response_mock.json.return_value = bike_new, 200
    return bike_new

@app.route('/bicicleta/<int:bicicleta_id>', methods=['DELETE'])
def deletar_bicicleta_route(bicicleta_id):
    is_delete = deletar_bicicleta(bicicleta_id)
    response_mock = Mock()
    if is_delete == True:
        response_mock.status_code = 200
        response_mock.json.return_value = dados_removidos, 200
    
    if is_delete == False:
        response_mock.status_code = 404
        response_mock.json.return_value = dados_nao_encontrados, 404

    return response_mock.json()


@app.route('/bicicleta/integrarNaRede', methods=['POST'])
def bicicleta_integrar_rede_route():
    data = request.json
    response_mock = Mock()

    validacao_tranca = validar_tranca_integrar_bicicleta(data['tranca_id'])
    validacao_bicicleta = integrar_bicicleta_rede(data['bicicleta_numero'])

    if not validacao_tranca or not validacao_bicicleta:
        response_mock.json.return_value = dados_invalidos, 422
        return response_mock.json()

    fechamento_da_tranca(data['tranca_id']) # enviar email

    response_mock.json.return_value = dados_cadastrados, 200
    return response_mock.json()


@app.route('/bicicleta/retirarDaRede', methods=['POST'])
def retirar_bicicleta_rede_route():
    data = request.json
    validar_bicicleta = retirar_bicicleta_rede(data)
    validar_tranca = validar_tranca_retirar_bicicleta(data)

    response_mock = Mock()
    if validar_bicicleta and validar_tranca:
        response_mock.json.return_value = dados_cadastrados, 200
        return response_mock.json()
    response_mock.json.return_value = dados_invalidos, 422
    return response_mock.json()


@app.route('/totem', methods=['GET'])
def listar_totens_route():
    return listar_totens()

@app.route('/totem/<int:totem_id>', methods=['GET'])
def listar_totem_id_route(totem_id):
    return listar_totem_id(totem_id)


@app.route('/totem', methods=['POST'])
def cadastrar_totem_route():
    totem = request.json
    cadastrar_totem(totem)

    response_mock = Mock()
    response_mock.status_code = dados_cadastrados, 200
    response_mock.json.return_value = request.json, 200
    return response_mock.json()


@app.route('/totem/<int:id_totem>', methods=['PUT'])
def editar_totem_route(id_totem):

    totem = request.json
    response_mock = Mock()

    response_mock.status_code = dados_atualizados, 200
    response_mock.json.return_value =  editar_totem(id_totem, totem), 200
    return response_mock.json()


@app.route('/totem/<int:id_totem>', methods=['DELETE'])
def deletar_totem_route(id_totem):
    is_delete = deletar_totem(id_totem)
    response_mock = Mock()
    if is_delete == True:
        response_mock.status_code = 200
        response_mock.json.return_value = dados_removidos, 200
    
    if is_delete == False:
        response_mock.status_code = 404
        response_mock.json.return_value = dados_nao_encontrados, 404

    return response_mock.json()

    

@app.route('/tranca', methods=['GET'])
def obter_trancas_route():
    return listar_trancas()


@app.route('/tranca/<int:tranca_id>', methods=['GET'])
def listar_tranca_id_route(tranca_id):
    return listar_tranca_id(tranca_id)


@app.route('/tranca', methods=['POST'])
def cadastrar_tranca_route():
    tranca = request.json
    cadastrar_tranca(tranca)

    response_mock = Mock()
    response_mock.status_code = dados_cadastrados, 200
    response_mock.json.return_value = request.json, 200
    return response_mock.json()


@app.route('/tranca/<int:id_tranca>', methods=['PUT'])
def editar_tranca_route(id_tranca):

    tranca = request.json
    response_mock = Mock()

    response_mock.status_code = dados_atualizados, 200
    response_mock.json.return_value =  editar_tranca(id_tranca, tranca), 200
    return response_mock.json()


@app.route('/tranca/<int:id_tranca>', methods=['DELETE'])
def deletar_tranca_route(id_tranca):
    is_delete = deletar_tranca(id_tranca)
    response_mock = Mock()
    if is_delete == True:
        response_mock.status_code = 200
        response_mock.json.return_value = dados_removidos, 200
    
    if is_delete == False:
        response_mock.status_code = 404
        response_mock.json.return_value = dados_nao_encontrados, 404

    return response_mock.json()


@app.route('/tranca/integrarNaRede', methods=['POST'])
def integrar_tranca_rede_route():
    data = request.json
    validar_tranca = integrar_tranca_rede(data)

    response_mock = Mock()
    if validar_tranca:
        response_mock.json.return_value = dados_cadastrados, 200
        return response_mock.json()
    response_mock.json.return_value = dados_invalidos, 422
    return response_mock.json()


@app.route('/tranca/retirarDaRede', methods=['POST'])
def retirar_tranca_rede_route():
    data = request.json
    validar_tranca = retirar_tranca_rede(data)

    response_mock = Mock()
    if validar_tranca:
        response_mock.json.return_value = dados_cadastrados, 200
        return response_mock.json()
    response_mock.json.return_value = dados_invalidos, 422
    return response_mock.json()


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
