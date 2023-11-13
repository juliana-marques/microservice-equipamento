import requests,  os, sys
from flask import Flask
from flask import request

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.BicicletaController import listar_bicicletas, cadastrar_bicicleta

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


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 4000)),host='0.0.0.0',debug=True)