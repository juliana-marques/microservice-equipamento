import os, sys
from flask import Flask,  request
from unittest.mock import Mock
from datetime import datetime

app = Flask(__name__)
requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)                                                                 

from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, deletar_bicicleta, listar_bicicleta_id, integrar_bicicleta_rede, retirar_bicicleta_rede, status_bicicleta
from service.TotemService import listar_totens, cadastrar_totem, deletar_totem, listar_totem_id, adicionar_tranca_totem
from service.TrancaService import listar_trancas, cadastrar_tranca, editar_tranca, deletar_tranca, listar_tranca_id, integrar_tranca_rede, retirar_tranca_rede, validar_tranca_integrar_bicicleta, fechamento_da_tranca, validar_tranca_retirar_bicicleta, status_trancar, status_destrancar
from model.bicicleta import Bicicleta
from model.tranca import Tranca
from model.totem import Totem

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

date = datetime.now()
data_horario = date.strftime("%d/%m/%Y %H:%M:%S")

@app.route('/bicicleta', methods=['GET'])
def listar_bicicletas_route():
    bicicletas = listar_bicicletas()
    if len(bicicletas) == 0:
        return "Não há bicicletas cadastradas", 200
    return bicicletas


@app.route('/bicicleta/<int:bicicleta_id>', methods=['GET'])
def listar_bicicleta_id_route(bicicleta_id):
    result = listar_bicicleta_id(bicicleta_id)
    response_mock = Mock()

    if result == False:
        response_mock.json.return_value = dados_nao_encontrados, 404
        return response_mock.json()
    
    response_mock.json.return_value = result, 200
    return response_mock.json()


@app.route('/bicicleta', methods=['POST'])
def cadastrar_bicicleta_route():
    """
    parâmetros:
        marca, modelo, ano, numero, status

    regras de negócio:
        - o numéro da bicicleta deve ser 0
        - o status atribuído deve ser o enum 3 (NOVA)
        - todos os dados devem ser preenchidos
    """

    response_mock = Mock()
    bicicleta = request.json

    json = ["numero", "marca", "modelo", "ano", "status"]

    response_mock.json.return_value = dados_invalidos, 422
    for data in json:
        if bicicleta.get(f"{data}") == None:
            return response_mock.json()
        
    status = Bicicleta().status_bicicleta(bicicleta["status"])
    if status != "NOVA":
        return response_mock.json()
    
    if bicicleta["numero"] != 0:
        return response_mock.json()
    
    bicicleta = cadastrar_bicicleta(bicicleta)
    
    response_mock.json.return_value = bicicleta, 200
    return response_mock.json()


@app.route('/bicicleta/<int:bicicleta_id>', methods=['PUT'])
def editar_bicicleta_route(bicicleta_id):
    """
    parâmetros:
        marca, modelo, ano, numero, status

    regras de negócio:
        - o número e o status não podem ser editados
        - todos os dados devem ser preenchidos
    """

    bicicleta = request.json
    response_mock = Mock()

    result = listar_bicicleta_id(bicicleta_id)
    if result == False:
        response_mock.json.return_value = dados_nao_encontrados, 404
        return response_mock.json()

    response_mock.json.return_value = dados_invalidos, 422

    json = ["marca", "modelo", "ano", "numero", "status"]
    for data in json:
        if bicicleta.get(f"{data}") == None:
            return response_mock.json()
        
    if bicicleta.get("numero") != 0:
        return response_mock.json()
        
    status = Bicicleta().status_bicicleta(bicicleta["status"])
    if status != result["status"]:
        return response_mock.json()

    bicicleta["numero"] = result["numero"]
    result = editar_bicicleta(bicicleta_id, bicicleta)
    if result == False:
        return response_mock.json()

    response_mock.status_code = "Dados atualizados", 200
    response_mock.json.return_value = result, 200
    return result


@app.route('/bicicleta/<int:bicicleta_id>', methods=['DELETE'])
def deletar_bicicleta_route(bicicleta_id):
    """
    parâmetros:
        - id

    regras de negócio:
        - apenas bicicletas com status aposentada
        AND
        - bicicletas que não estão em nenhuma tranca
    """

    response_mock = Mock()
    response_mock.json.return_value = dados_nao_encontrados, 404

    result = listar_bicicleta_id(bicicleta_id)
    if result == False:
        return response_mock.json()
    
    status = Bicicleta().status_bicicleta(result.get("status"))
    if status != "APOSENTADA": ## AND NENHUMA TRANCA
        response_mock.json.return_value = "Status inválido", 422
        return response_mock.json()

    is_delete = deletar_bicicleta(bicicleta_id)
    if is_delete == True:
        response_mock.status_code = 200
        response_mock.json.return_value = dados_removidos, 200
    
    return response_mock.json()


################################################################################
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


@app.route('/bicicleta/<int:bicicleta_id>/status/<int:acao>', methods=['POST'])
def status_bicicleta_route(bicicleta_id, acao): 
    validar_bicicleta = status_bicicleta(bicicleta_id, acao)

    response_mock = Mock()
    if validar_bicicleta:
        response_mock.json.return_value = dados_cadastrados, 200
        return response_mock.json()
    response_mock.json.return_value = dados_invalidos, 422
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
################################################################################

@app.route('/totem', methods=['GET'])
def listar_totens_route():
    totens = listar_totens()
    if len(totens) == 0:
        return "Não há totens cadastrados", 200
    return totens


@app.route('/totem/<int:totem_id>', methods=['GET'])
def listar_totem_id_route(totem_id):
    result = listar_totem_id(totem_id)
    response_mock = Mock()

    if result == False:
        response_mock.json.return_value = dados_nao_encontrados, 404
        return response_mock.json()
    
    response_mock.json.return_value = result, 200
    return response_mock.json()


@app.route('/totem', methods=['POST'])
def cadastrar_totem_route():
    """
    parâmetros:
        localizacao, descricao

    regras de negócio:
        - todos os dados devem ser preenchidos
    """

    response_mock = Mock()
    totem = request.json

    json = ["localizacao", "descricao"]
    response_mock.json.return_value = dados_invalidos, 422
    for data in json:
        if totem.get(f"{data}") == None:
            return response_mock.json()
        

    totem = cadastrar_totem(totem)

    response_mock.json.return_value = totem, 200
    return response_mock.json()


@app.route('/totem/<int:id_totem>', methods=['DELETE'])
def deletar_totem_route(id_totem):
    """
    parâmetros:
        - id

    regras de negócio:
        - totens que não possuem tranca
    """

    is_delete = deletar_totem(id_totem)
    response_mock = Mock()
    if is_delete == True:
        response_mock.status_code = 200
        response_mock.json.return_value = dados_removidos, 200
    
    if is_delete == False:
        response_mock.status_code = 404
        response_mock.json.return_value = dados_nao_encontrados, 404

    return response_mock.json()

######## listar bicicletas e trancas NOS TOTENS

@app.route('/tranca', methods=['GET'])
def obter_trancas_route():
    trancas = listar_trancas()
    if len(trancas) == 0:
        return "Não há trancas cadastradas", 200
    return trancas


@app.route('/tranca/<int:tranca_id>', methods=['GET'])
def listar_tranca_id_route(tranca_id):
    result = listar_tranca_id(tranca_id)
    response_mock = Mock()

    if result == False:
        response_mock.json.return_value = dados_nao_encontrados, 404
        return response_mock.json()
    
    response_mock.json.return_value = result, 200
    return response_mock.json()


@app.route('/tranca', methods=['POST'])
def cadastrar_tranca_route():
    """
    parâmetros:
        numero, localizacao, ano_de_fabricacao, modelo, status

    regras de negócio:
        - o numéro da tranca deve ser 0
        - o status atribuído deve ser o enum 1 (NOVA)
        - todos os dados devem ser preenchidos
    """

    response_mock = Mock()
    response_mock.json.return_value = dados_invalidos, 422

    tranca = request.json

    json = ["numero", "localizacao", "ano_de_fabricacao", "modelo", "status"]
    for data in json:
        if tranca.get(f"{data}") == None:
            return response_mock.json()

    status = Tranca().status_tranca(tranca["status"])
    if status != "NOVA":
        return response_mock.json()

    if tranca["numero"] != 0:
        return response_mock.json()
    
    tranca = cadastrar_tranca(tranca)

    response_mock.json.return_value = tranca, 200
    return response_mock.json()


@app.route('/tranca/<int:id_tranca>', methods=['PUT'])
def editar_tranca_route(id_tranca):
    """
    parâmetros:
        numero, localizacao, ano_de_fabricacao, modelo, status

    regras de negócio:
        - o número e o status não podem ser editados
        - todos os dados devem ser preenchidos
    """

    tranca = request.json
    response_mock = Mock()

    
    result = listar_tranca_id(id_tranca)
    if result == False:
        response_mock.json.return_value = dados_nao_encontrados, 404
        return response_mock.json()
    
    response_mock.json.return_value = dados_invalidos, 422

    json = ["numero", "localizacao", "ano_de_fabricacao", "modelo", "status"]
    for data in json:
        if tranca.get(f"{data}") == None:
            return response_mock.json()
        
    if tranca["numero"] != 0:
        return response_mock.json()
    
    status = Tranca().status_tranca(tranca["status"])
    if status != result["status"]:
        return response_mock.json()
    
    tranca["numero"] = result["numero"]
    result = editar_tranca(id_tranca, tranca)

    response_mock.status_code = dados_atualizados, 200
    response_mock.json.return_value =  editar_tranca(id_tranca, tranca), 200
    return response_mock.json()


@app.route('/tranca/<int:id_tranca>', methods=['DELETE'])
def deletar_tranca_route(id_tranca):
    """
    parâmetros:
        - id

    regras de negócio:
        - apenas trancas sem bicicleta
    """

    response_mock = Mock()
    response_mock.json.return_value = dados_nao_encontrados, 404

    result = listar_tranca_id(id_tranca)
    if result == False:
        return response_mock.json()
    
    ## TRANCAS SEM BICICLETA

    is_delete = deletar_tranca(id_tranca)
    if is_delete == True:
        response_mock.json.return_value = dados_removidos, 200

    return response_mock.json()


@app.route('/tranca/integrarNaRede', methods=['POST'])
def integrar_tranca_rede_route():
    response_mock = Mock()
    response_mock.json.return_value = dados_invalidos, 422

    response = request.json

    json = ["id_totem", "id_tranca", "id_funcionario"]
    for data in json:
        if response.get(f"{data}") == None:
            return response_mock.json()
    
    tranca = listar_tranca_id(response["id_tranca"])
    if tranca == False:
        return response_mock.json()
    
    totem = listar_totem_id(response["id_totem"])
    if totem == False:
        return response_mock.json()
    
    print(tranca["status"])
    if tranca["status"] == "NOVA" or tranca["status"] == "EM_REPARO":
        tranca_rede = integrar_tranca_rede(tranca)
        adicionar_tranca_totem(response["id_totem"], tranca_rede, data_horario)
        response_mock.json.return_value = dados_cadastrados, 200

    # ENVIA MENSAGEM PARA O REPARADOR 

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


@app.route('/tranca/<int:id_tranca>/trancar', methods=['POST'])
def trancar_route(id_tranca):
    response_mock = Mock()
    response_mock.json.return_value = dados_invalidos, 422

    tranca = listar_tranca_id(id_tranca)
    if tranca == False:
        response_mock.json.return_value = dados_nao_encontrados, 422
        return response_mock.json()
    
    data = request.json
    if len(data) == 1:
        if data.get("bicicleta") == None:
            return response_mock.json()
        else:
            tranca["bicicleta"] = data["bicicleta"]

    status_trancar(tranca)
    response_mock.json.return_value = dados_cadastrados, 200
    return response_mock.json()


@app.route('/tranca/<int:id_tranca>/destrancar', methods=['POST'])
def destrancar_route(id_tranca):
    response_mock = Mock()
    response_mock.json.return_value = dados_invalidos, 422

    tranca = listar_tranca_id(id_tranca)
    if tranca == False:
        response_mock.json.return_value = dados_nao_encontrados, 422
        return response_mock.json()
    
    data = request.json
    if len(data) == 1:
        if data.get("bicicleta") == None:
            return response_mock.json()
        else:
            tranca["bicicleta"] = data["bicicleta"]

    status_destrancar(tranca)
    response_mock.json.return_value = dados_cadastrados, 200
    return response_mock.json()


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
