from unittest.mock import Mock

requests = Mock()

def listar_bicicletas():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = [
            {
                "id": 1,
                "marca": "adidas",
                "modelo": "fina",
                "ano": "2023",
                "numero": 1,
                "status": "DISPONIVEL"
            },
            {
                "id": 2,
                "marca": "nike",
                "modelo": "grossa",
                "ano": "2022",
                "numero": 1,
                "status": "EM_USO"
            },
        ]
    

    return response_mock.json()


def cadastrar_bicicleta(marca, modelo, ano, numero, status):
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
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "numero": numero,
        "status": status
    }

    return response_mock.json()

def editar_bicicleta(id, marca, modelo, ano, numero, status):
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
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "numero": numero,
        "status": status
    }

    return response_mock.json()


def deletar_bicicleta(bicicleta_id):

    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = "Dados removidos"

    bicicletas = listar_bicicletas()
    for bicicleta in bicicletas:
        if bicicleta['id'] == bicicleta_id:
            bicicletas.remove(bicicleta)
            return response_mock.json()
    
    response_mock.status_code = 422
    response_mock.json.return_value = [
        {
            "codigo": 404,
            "mensagem": "Não encontrado"
        }
    ]

    return response_mock.json()


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