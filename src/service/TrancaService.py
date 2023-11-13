import logging, mock
from unittest.mock import Mock



def listar_trancas():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = [
    {
        "id": 1,
        "bicicleta": 101,
        "numero": 1,
        "localizacao": "Botafogo",
        "anoDeFabricacao": "2022",
        "modelo": "Modelo A",
        "status": "Disponível"
    },
    {
        "id": 2,
        "bicicleta": 102,
        "numero": 2,
        "localizacao": "Flamengo",
        "anoDeFabricacao": "2021",
        "modelo": "Modelo B",
        "status": "Ocupada"
    },
    {
        "id": 3,
        "bicicleta": 103,
        "numero": 3,
        "localizacao": "Copacabana",
        "anoDeFabricacao": "2023",
        "modelo": "Modelo C",
        "status": "Disponível"
    }
    ]
    return response_mock.json()


def cadastrar_tranca(numero, localizacao, anoDeFabricacao, modelo, status):
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
        "numero": numero,
        "localizacao": localizacao,
        "anoDeFabricacao": anoDeFabricacao,
        "modelo":  modelo,
        "status": status
    }
    return response_mock.json()

def buscar_tranca_por_id(idTranca):
    response_mock = Mock()
    response_mock.status_code = "Tranca encontrada", 200
    idExists = validar_id(idTranca)

    if idExists == False:
        response_mock.status_code = 404
        response_mock.json.return_value = [
            {
                "codigo": response_mock.status_code,
                "mensagem": "Não encontrado"
            }
        ]
    trancas = listar_trancas()
    
    for tranca in trancas:
        if tranca['numero'] == idTranca:
            response_mock.json.return_value = tranca
            return response_mock.json.return_value

def validar_id(idTranca):
    trancas = listar_trancas()
    for tranca in trancas:
        if tranca.numero == idTranca:
            return True