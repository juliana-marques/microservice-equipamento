import logging, mock
from unittest.mock import Mock

requests = Mock()

def listar_bicicletas():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = {
        "bicicletas": [
            {
                "id": 1,
                "marca": "adidas",
                "modelo": "fina",
                "ano": "2023",
                "numero": 1,
                "status": "disponível"
            },
            {
                "id": 2,
                "marca": "nike",
                "modelo": "grossa",
                "ano": "2022",
                "numero": 1,
                "status": "utilizada"
            },
        ]
    }

    return response_mock.json()

#def cadastrar_bicicleta():
    