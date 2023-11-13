import unittest, os, sys
from unittest.mock import patch, Mock

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, validar_id, deletar_bicicleta

class TestBicicletaService(unittest.TestCase):
    @patch('service.BicicletaService.Mock')
    def test_listar_bicicletas(self, mock_request):

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
        

        mock_request.return_value = response_mock

        result = listar_bicicletas()
        self.assertEqual(len(result), 2) 

    @patch('service.BicicletaService.Mock')
    def test_cadastrar_bicicleta(self, mock_request):
        marca = "TesteMarca"
        modelo = "TesteModelo"
        ano = "2023"
        numero = 3
        status = "DISPONIVEL"
        
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "id": 3,
            "marca": marca,
            "modelo": modelo,
            "ano": ano,
            "numero": numero,
            "status": status
        }

        mock_request.return_value = response_mock

        result = cadastrar_bicicleta(marca, modelo, ano, numero, status)
        self.assertEqual(result['marca'], marca)  
        self.assertEqual(result['status'], status)

    @patch('service.BicicletaService.Mock')
    def test_editar_bicicleta(self, mock_request):
        id_bicicleta = 1  
        marca = "NovaMarca"
        modelo = "NovoModelo"
        ano = "2024"
        numero = 2
        status = "EM_USO"

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "id": id_bicicleta,
            "marca": marca,
            "modelo": modelo,
            "ano": ano,
            "numero": numero,
            "status": status
        }

        mock_request.return_value = response_mock

        result = editar_bicicleta(id, marca, modelo, ano, numero, status)
        self.assertEqual(result['marca'], marca)
        self.assertEqual(result['ano'], ano)

if __name__ == '__main__':
    unittest.main()