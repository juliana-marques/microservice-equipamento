import os, sys
from flask import Flask,  request
from unittest.mock import Mock

app = Flask(__name__)
requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)                                                                 


from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, validar_id, deletar_bicicleta
from service.TotemService import listar_totens, cadastrar_totem, editar_totem, validar_id_totem, deletar_totem
from service.TrancaService import listar_trancas, cadastrar_tranca, buscar_tranca_por_id, editar_tranca, deletar_tranca


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

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World! :)"


@app.route('/bicicleta', methods=['GET'])
def listar_bicicletas_route():
    return listar_bicicletas()


@app.route('/bicicleta', methods=['POST'])
def cadastrar_bicicleta_route():
    data = request.json
    marca, modelo, ano, numero, status = data.get('marca'), data.get('modelo'), data.get('ano'), data.get('numero'), data.get('status')
    return cadastrar_bicicleta(marca, modelo, ano, numero, status)


@app.route('/bicicleta/<int:bicicleta_id>', methods=['PUT'])
def editar_bicicleta_route(bicicleta_id):
    verificacao = validar_id(bicicleta_id)
    if verificacao != True:
        return verificacao

    data = request.json
    marca, modelo, ano, numero, status = data.get('marca'), data.get('modelo'), data.get('ano'), data.get('numero'), data.get('status')
    return editar_bicicleta(bicicleta_id, marca, modelo, ano, numero, status)


@app.route('/bicicleta/<int:bicicleta_id>', methods=['DELETE'])
def deletar_bicicleta_route(bicicleta_id):
    return deletar_bicicleta(bicicleta_id)


@app.route('/totem', methods=['GET'])
def listar_totens_route():
    return listar_totens()


@app.route('/totem', methods=['POST'])
def cadastrar_totem_route():
    data = request.json

    localizacao, descricao = data.get('localizacao'), data.get('descricao')
    return cadastrar_totem(localizacao, descricao)


@app.route('/totem/<int:id_totem>', methods=['PUT'])
def editar_totem_route(id_totem):

    verificacao = validar_id_totem(id_totem)
    if verificacao != True:
        return verificacao

    data = request.json
    localizacao, descricao = data.get('localizacao'), data.get('descricao')

    return editar_totem(id_totem, localizacao, descricao)


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

    return cadastrar_tranca(numero, localizacdao, ano_de_fabricacao, modelo, status)


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

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
