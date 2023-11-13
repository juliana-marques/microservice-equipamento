import logging, mock, unittest
from unittest.mock import Mock, MagicMock

requests = Mock()

def listar_totens():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = [
            {
                "id": 1,
                "localizacao": "Rio de Janeiro",
                "descricao": "Descricao nada criativa"
            },
            {
                "id": 2,
                "localizacao": "Rio de Janeiro",
                "descricao": "Descricao nada criativa"
            },
        ]
    

    return response_mock.json()

def cadastrar_totem(localizacao, descricao):
    response_mock = Mock()
    response_mock.status_code = "Dados cadastrados", 200

    validacao = True

    if validacao == False:

        response_mock.status_code = 422
        response_mock.json.return_value = [
            {
                "codigo": 422,
                "mensagem": "Dados inválidos"
            }
        ]
        return response_mock.json()
    
    response_mock.json.return_value = {
        "id": 3,
        "localizacao": localizacao,
        "descricao": descricao
    }

    return response_mock.json()

def editar_totem(id, localizacao, descricao):
    response_mock = Mock()
    response_mock.status_code = "Dados atualizados", 200

    validacao = True

    if validacao == False:

        response_mock.status_code = 422
        response_mock.json.return_value = [
            {
                "codigo": 422,
                "mensagem": "Dados inválidos."
            }
        ]
        return response_mock.json()
    
    response_mock.json.return_value = {
        "id": id,
        "localizacao": localizacao,
        "descricao": descricao
    }

    return response_mock.json()

def validar_id_totem(idTotem):
    totens = listar_totens()

    for totem in totens:
        if totem['id'] == idTotem:
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

def deletar_totem(idTotem):
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = "Dados removidos"

    totens = listar_totens()
    for totem in totens:
        if totem['id'] == idTotem:
            totens.remove(totem)
            return response_mock.json()
    
    response_mock.status_code = 422
    response_mock.json.return_value = [
        {
            "codigo": 404,
            "mensagem": "Não encontrado"
        }
    ]

    return response_mock.json()