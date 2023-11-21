from unittest.mock import Mock
import os, sys

requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)     

from repository.totem_repository import TotemRepository as repository
 

def listar_totens():
    return repository().listar_totens()


def cadastrar_totem(totem):
    repository().adicionar_totem(totem)

def editar_totem(id, totem):
    totens = repository().listar_totens()

    for t in totens:
        if t['id'] == id:
            totem['id'] = id
            repository().deletar_totem(id)
            repository().adicionar_totem(totem)

    return totem


def validar_id_totem(id_totem):
    totens = listar_totens()
    for totem in totens:
        if totem['id'] == id_totem:
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


def deletar_totem(id_totem):
   
    return repository.deletar_totem(id_totem)