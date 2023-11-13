import requests, mock, os
from flask import Flask
from flask import request
from unittest.mock import Mock
from controller.BicicletaController import listar_bicicletas#, cadastrar_bicicleta

requests = Mock()


app = Flask(__name__)


@app.route('/bicicleta', methods=['GET'])
def listar_bicicletas_route():
    bicicletas = listar_bicicletas()
    return bicicletas


#@app.route('/bicicleta', methods=['POST'])
#def cadastrar_bicicleta_route(marca, modelo, ano, numero, status):
#    cadastrar_bicicleta()


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 4000)),host='0.0.0.0',debug=True)