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
        "ano_de_fabricacao": "2022",
        "modelo": "Modelo A",
        "status": "Disponível"
    },
    {
        "id": 2,
        "bicicleta": 102,
        "numero": 2,
        "localizacao": "Flamengo",
        "ano_de_fabricacao": "2021",
        "modelo": "Modelo B",
        "status": "Ocupada"
    },
    {
        "id": 3,
        "bicicleta": 103,
        "numero": 3,
        "localizacao": "Copacabana",
        "ano_de_fabricacao": "2023",
        "modelo": "Modelo C",
        "status": "Disponível"
    }
    ]
    return response_mock.json()


def cadastrar_tranca(numero, localizacao, ano_de_fabricacao, modelo, status):
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
        "ano_de_fabricacao": ano_de_fabricacao,
        "modelo":  modelo,
        "status": status
    }
    return response_mock.json()

def buscar_tranca_por_id(id_tranca):
    response_mock = Mock()
    id_exists = validar_id(id_tranca)

    if id_exists == False:
        response_mock.status_code = 404
        response_mock.json.return_value = {
            "codigo": 404,
            "mensagem": "Não encontrado."
        }

        return response_mock.json()
        
   
    trancas = listar_trancas()
    for tranca in trancas:
        if tranca['numero'] == id_tranca:
            response_mock.json.return_value = tranca
            response_mock.status_code = "Encontrado", 200
    return response_mock.json()


def editar_tranca(data, id_tranca):
    response_mock = Mock()
    tranca = buscar_tranca_por_id(id_tranca)
    response_mock.status_code = "Dados atualizados", 200
    idExists = validar_id(id_tranca)

    numero = data.get('numero')
    localizacao = data.get('localizacao')
    anoDeFabricacao = data.get('anoDeFabricacao')
    modelo = data.get('modelo')
    status = data.get('status')

    if idExists == False:
        response_mock.status_code = 404
        response_mock.json.return_value = [
            {
                "codigo": response_mock.status_code,
                "mensagem": "Não encontrado"
            }
        ]
        return response_mock.json()
    
    tranca['numero'] = numero
    tranca['localizacao'] = localizacao
    tranca['anoDeFabricacao'] = anoDeFabricacao
    tranca['modelo'] = modelo
    tranca['status'] = status
    
    return tranca


def deletar_tranca(id_tranca):
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = "Tranca removida"
    trancas = listar_trancas()
    for tranca in trancas:
        if tranca['numero'] == id_tranca:
            trancas.remove(tranca)
            return response_mock.json()
        
def validar_id(id_tranca):
    trancas = listar_trancas()
    for tranca in trancas:
        if tranca['numero'] == id_tranca:
            return True
    return False