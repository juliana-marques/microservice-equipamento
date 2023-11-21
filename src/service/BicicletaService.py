from unittest.mock import Mock
import os, sys

requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)     

from repository.bicicleta_repository import BicletaRepository as repository

def listar_bicicletas():
    return repository().listar_bicicleta()


def cadastrar_bicicleta(bicicleta):
    repository().adicionar_bicicleta(bicicleta)
    

def editar_bicicleta(id_bicicleta, bicicleta):
    bicicletas = repository().listar_bicicleta()
    
    for b in bicicletas:
        if b['id'] == id_bicicleta:
            bicicleta['id'] = id_bicicleta
            repository().deletar_bicicleta(id_bicicleta)
            repository().adicionar_bicicleta(bicicleta)
    return bicicleta
    

def deletar_bicicleta(bicicleta_id):
    return repository().deletar_bicicleta(bicicleta_id)


def validar_id(bicicleta_id):
    bicicletas = listar_bicicletas()

    for bicicleta in bicicletas:
        if bicicleta['id'] == bicicleta_id:
            return True
        
    response_mock = Mock()
    response_mock.status_code = 422
    response_mock.json.return_value = [
        {
            "codigo": 404,
            "mensagem": "Não encontrado."
        }
    ]
    return response_mock.json()