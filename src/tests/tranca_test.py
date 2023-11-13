import unittest, os, sys
from unittest.mock import patch, Mock

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.TrancaService import listar_trancas, cadastrar_tranca, buscar_tranca_por_id, editar_tranca, deletar_tranca

class TestTrancaService(unittest.TestCase):
    @patch('service.TrancaService.Mock')
    def test_listar_tranca(self, mock_request):

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

        mock_request.return_value = response_mock

        result = listar_trancas()
        self.assertEqual(len(result), 3) 

    @patch('service.TrancaService.Mock')
    def test_cadastrar_bicicleta(self, mock_request):

        bicicleta = 103,
        numero = 4,
        localizacao = "Copacabana",
        ano_de_fabricacao = "2023",
        modelo = "Modelo C",
        status = "DISPONIVEL"
        
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "id": 4,
            "bicicleta": bicicleta,
            "numero": numero,
            "localizacao": localizacao,
            "ano_de_fabricacao": ano_de_fabricacao,
            "modelo": modelo,
            "status": status
        }

        mock_request.return_value = response_mock

        result = cadastrar_tranca(numero, localizacao, ano_de_fabricacao, modelo, status)
        self.assertEqual(result['modelo'], modelo)  
        self.assertEqual(result['status'], status)

    @patch('service.TrancaService.Mock')
    def test_editar_tranca(self, mock_request):
        id_tranca = 1  
        bicicleta = 103,
        numero = 7,
        localizacao = "Rio",
        ano_de_fabricacao = "2023",
        modelo = "Modelo C",
        status = "DISPONIVEL"

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "id": id_tranca,
            "bicicleta": bicicleta,
            "numero": numero,
            "localizacao": localizacao,
            "ano_de_fabricacao": ano_de_fabricacao,
            "modelo": modelo,
            "status": status
        }

        mock_request.return_value = response_mock

        result = editar_tranca(id_tranca)
        self.assertEqual(result['modelo'], modelo)
        self.assertEqual(result['ano_de_fabricacao'], ano_de_fabricacao)

if __name__ == '__main__':
    unittest.main()