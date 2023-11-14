import unittest, os, sys
from unittest.mock import patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app

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

        data = {
            "id": 3,
            "marca": "teste",
            "modelo": "teste",
            "ano": "teste",
            "numero": "teste",
            "status": "teste"
        }
        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.post('/bicicleta', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=data)
            self.assertEqual(response.status_code, mock_cadastrar_bicicletas.status_code)


    @patch('controller.main.Mock')
    def test_editar_bicicletas_route(self, mock_editar_bicicletas):

        mock_editar_bicicletas.status_code = 200

        data = {
            "id": 2,
            "marca": "teste",
            "modelo": "teste",
            "ano": "teste",
            "numero": "teste",
            "status": "teste"
        }
        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.put('/bicicleta/2', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=data)
            self.assertEqual(response.status_code, mock_editar_bicicletas.status_code)


    @patch('controller.main.Mock')
    def test_deletar_bicicletas_route(self, mock_deletar_bicicletas):

        mock_deletar_bicicletas.status_code = 200
        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.delete('/bicicleta/2', headers={"Content-Type": "application/json", "X-CSRFToken": token})
            self.assertEqual(response.status_code, mock_deletar_bicicletas.status_code)


    @patch('controller.main.Mock')
    def test_listar_totem_route(self, mock_listar_totem):

        mock_listar_totem.status_code = 200
        with app.test_client() as client:
            response = client.get('/totem')
            self.assertEqual(response.status_code, mock_listar_totem.status_code)


    @patch('controller.main.Mock')
    def test_cadastrar_totem_route(self, mock_cadastrar_totem):

        mock_cadastrar_totem.status_code = 200

        data = {
            "id": 1,
            "localizacao": "teste",
            "descricao": "teste"
        }
        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.post('/totem', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=data)
            self.assertEqual(response.status_code, mock_cadastrar_totem.status_code)


    @patch('controller.main.Mock')
    def test_editar_totem_route(self, mock_editar_totem):

        mock_editar_totem.status_code = 200

        data = {
            "id": 1,
            "localizacao": "teste",
            "descricao": "teste"
        }
        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.put('/totem/1', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=data)
            self.assertEqual(response.status_code, mock_editar_totem.status_code)


    @patch('controller.main.Mock')
    def test_deletar_totem_route(self, mock_deletar_totem):

        mock_deletar_totem.status_code = 200

        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.delete('/totem/1', headers={"Content-Type": "application/json", "X-CSRFToken": token})
            self.assertEqual(response.status_code, mock_deletar_totem.status_code)


    @patch('controller.main.Mock')
    def test_listar_tranca_route(self, mock_listar_tranca):

        mock_listar_tranca.status_code = 200
        with app.test_client() as client:
            response = client.get('/tranca')
            self.assertEqual(response.status_code, mock_listar_tranca.status_code)


    @patch('controller.main.Mock')
    def test_cadastrar_tranca_route(self, mock_cadastrar_tranca):

        mock_cadastrar_tranca.status_code = 200

        data = {
            "id": 2,
            "numero": "teste",
            "localizacao": "teste",
            "ano_de_fabricacao": "teste",
            "modelo": "teste",
            "status": "teste"
        }
        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.post('/tranca', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=data)
            self.assertEqual(response.status_code, mock_cadastrar_tranca.status_code)


    @patch('controller.main.Mock')
    def test_editar_tranca_route(self, mock_editar_tranca):

        mock_editar_tranca.status_code = 200

        data = {
            "id": 3,
            "numero": "teste",
            "localizacao": "teste",
            "ano_de_fabricacao": "teste",
            "modelo": "teste",
            "status": "teste"
        }
        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.put('/tranca/2', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=data)
            self.assertEqual(response.status_code, mock_editar_tranca.status_code)


    @patch('controller.main.Mock')
    def test_deletar_tranca_route(self, mock_deletar_tranca):

        mock_deletar_tranca.status_code = 200
        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.delete('/tranca/2', headers={"Content-Type": "application/json", "X-CSRFToken": token})
            self.assertEqual(response.status_code, mock_deletar_tranca.status_code)


if __name__ == '__main__':
    unittest.main()