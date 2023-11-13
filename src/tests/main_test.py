import unittest, os, sys
from unittest.mock import patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app
from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, validar_id, deletar_bicicleta

class TestMain(unittest.TestCase):

    @patch('controller.main.Mock')
    def test_listar_bicicletas_route(self, mock_listar_bicicletas):

        mock_listar_bicicletas.status_code = 200

        with app.test_client() as client:
            response = client.get('/bicicleta')

            self.assertEqual(response.status_code, mock_listar_bicicletas.status_code)

    @patch('controller.main.Mock')
    def test_cadastrar_bicicletas_route(self, mock_cadastrar_bicicletas):

        mock_cadastrar_bicicletas.status_code = 200

        with app.test_client() as client:
            response = client.post('/bicicleta')

            self.assertEqual(response.status_code, mock_cadastrar_bicicletas.status_code)
if __name__ == '__main__':
    unittest.main()