import unittest
from unittest.mock import Mock, patch
from service.TrancaService import listar_trancas, cadastrar_tranca, buscar_tranca_por_id, editar_tranca, deletar_tranca, validar_id

from your_module import (
    listar_trancas,
    cadastrar_tranca,
    buscar_tranca_por_id,
    editar_tranca,
    deletar_tranca,
    validar_id
)

modelo_a = "Modelo A"
disponivel = "DISPONIVEL"

class TestAppFunctions(unittest.TestCase):

    @patch('your_module.Mock')
    def test_listar_trancas(self, mock_response):
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": 1,
                "bicicleta": 101,
                "numero": 1,
                "localizacao": "Botafogo",
                "ano_de_fabricacao": "2022",
                "modelo": modelo_a,
                "status": disponivel
            },
            {
                "id": 2,
                "bicicleta": 102,
                "numero": 2,
                "localizacao": "Flamengo",
                "ano_de_fabricacao": "2021",
                "modelo": "Modelo B",
                "status": "Ocupada"
            }
            
        ]

        with patch('your_module.listar_trancas', return_value=mock_response.json()):
            result = listar_trancas()

        self.assertEqual(result, mock_response.json())

    @patch('your_module.Mock')
    def test_cadastrar_tranca(self, mock_response):
        numero = 1
        localizacao = "Botafogo"
        ano_de_fabricacao = "2022"
        modelo = modelo_a
        status = disponivel

        mock_response.status_code = 200
        mock_response.json.return_value = {
            "numero": numero,
            "localizacao": localizacao,
            "ano_de_fabricacao": ano_de_fabricacao,
            "modelo": modelo,
            "status": status
        }

        with patch('your_module.cadastrar_tranca', return_value=mock_response.json()):
            result = cadastrar_tranca(numero, localizacao, ano_de_fabricacao, modelo, status)

        self.assertEqual(result, mock_response.json())

    @patch('your_module.Mock')
    def test_buscar_tranca_por_id(self, mock_response):
        # Mocking the ID for testing
        id_tranca = 1

        # Mocking the response from your service function
        mock_response.status_code = "Encontrado", 200
        mock_response.json.return_value = {
            "id": id_tranca,
            "bicicleta": 101,
            "numero": id_tranca,
            "localizacao": "Botafogo",
            "ano_de_fabricacao": "2022",
            "modelo": modelo_a,
            "status": disponivel
        }

        with patch('your_module.buscar_tranca_por_id', return_value=mock_response.json()):
            result = buscar_tranca_por_id(id_tranca)

        self.assertEqual(result, mock_response.json())

    # Add tests for other functions like editar_tranca, deletar_tranca, and validar_id here
    @patch('your_module.Mock')
    def test_editar_tranca(self, mock_response):
        # Mocking the ID for testing
        id_tranca = 1

        # Mocking the input data
        data = {
            "numero": 1,
            "localizacao": "Copacabana",
            "ano_de_fabricacao": "2022",
            "modelo": modelo_a,
            "status": "Ocupada"
        }

        # Mocking the response from your service function
        mock_response.status_code = "Dados atualizados", 200
        mock_response.json.return_value = data

        with patch('your_module.editar_tranca', return_value=mock_response.json()):
            result = editar_tranca(data, id_tranca)

        self.assertEqual(result, mock_response.json())

    @patch('your_module.Mock')
    def test_deletar_tranca(self, mock_response):
        # Mocking the ID for testing
        id_tranca = 1

        # Mocking the response from your service function
        mock_response.status_code = 200
        mock_response.json.return_value = "Tranca removida"

        with patch('your_module.deletar_tranca', return_value=mock_response.json()):
            result = deletar_tranca(id_tranca)

        self.assertEqual(result, mock_response.json())

    @patch('your_module.Mock')
    def test_validar_id(self, mock_response):
        # Mocking the ID for testing
        id_tranca = 1

        # Mocking the response from your service function
        mock_response.status_code = 200
        mock_response.json.return_value = True

        with patch('your_module.validar_id', return_value=mock_response.json()):
            result = validar_id(id_tranca)

        self.assertEqual(result, mock_response.json())
if __name__ == '__main__':
    unittest.main()
