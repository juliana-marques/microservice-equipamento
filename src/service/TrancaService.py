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
        "localizacao": "Garagem",
        "anoDeFabricacao": "2022",
        "modelo": "Modelo A",
        "status": "Disponível"
    },
    {
        "id": 2,
        "bicicleta": 102,
        "numero": 2,
        "localizacao": "Quintal",
        "anoDeFabricacao": "2021",
        "modelo": "Modelo B",
        "status": "Ocupada"
    },
    {
        "id": 3,
        "bicicleta": 103,
        "numero": 3,
        "localizacao": "Armário",
        "anoDeFabricacao": "2023",
        "modelo": "Modelo C",
        "status": "Disponível"
    }
    ]
    return response_mock.json()