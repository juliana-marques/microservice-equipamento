import unittest, os, sys
from unittest.mock import patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.controller.main import app
from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, validar_id, deletar_bicicleta

class TestMain(unittest.TestCase):

    @patch('main.listar_bicicletas')
    def test_listar_bicicletas_route(self, mock_listar_bicicletas):

        mock_listar_bicicletas.return_value = "Bicicletas listadas"

        with app.test_client() as client:
            response = client.get('/bicicleta')

            self.assertEqual(response.data.decode(), "Bicicletas listadas")

if __name__ == '__main__':
    unittest.main()