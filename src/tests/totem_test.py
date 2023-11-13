import unittest, os, sys
from unittest.mock import patch, Mock

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.TotemService import listar_totens, cadastrar_totem, editar_totem, validar_id_totem, deletar_totem

class TestTotemService(unittest.TestCase):
    @patch('service.TotemService.Mock')
    def test_listar_totens(self, mock_request):

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
        

        mock_request.return_value = response_mock

        result = listar_totens()
        self.assertEqual(len(result), 2) 

    @patch('service.TotemService.Mock')
    def test_cadastrar_totem(self, mock_request):
        localizacao = "TesteLoc"
        descricao = "TesteDesc"
        
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "id": 3,
            "localizacao": localizacao,
            "descricao": descricao
        }

        mock_request.return_value = response_mock

        result = cadastrar_totem(localizacao, descricao)
        self.assertEqual(result['localizacao'], localizacao)  
        self.assertEqual(result['descricao'], descricao)

    @patch('service.TotemService.Mock')
    def test_editar_totem(self, mock_request):
        id_totem = 1  
        localizacao = "localizacao"
        descricao = "descricao"

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "id": id_totem,
            "localizacao": localizacao,
            "descricao": descricao
        }

        mock_request.return_value = response_mock

        result = editar_totem(id, localizacao, descricao)
        self.assertEqual(result['localizacao'], localizacao)
        self.assertEqual(result['descricao'], descricao)

if __name__ == '__main__':
    unittest.main()