import unittest, os, sys, json
from unittest.mock import Mock, patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app
from service.BicicletaService import listar_bicicleta_id
from service.TotemService import listar_totem_id
from service.TrancaService import listar_tranca_id
from repository.bicicleta_repository import BicletaRepository
from repository.totem_repository import TotemRepository
from repository.tranca_repository import TrancaRepository


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_listar_bicicletas_route(self):
        response = self.client.get('/bicicleta')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        bicicletas_esperadas = BicletaRepository().listar_bicicleta()
        self.assertEqual(data, bicicletas_esperadas)


    def test_listar_bicicleta_id_route(self):
        response = self.client.get('/bicicleta/1')
        data = response.text

        bicicletas_esperadas = listar_bicicleta_id(1)
        self.assertEqual(data, bicicletas_esperadas)


    def test_listar_totens_route(self):
        response = self.client.get('/totem')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        totens_esperados = TotemRepository().listar_totens()
        self.assertEqual(data, totens_esperados)


    def test_listar_totens_id_route(self):
        response = self.client.get('/totem/1')
        data = response.text

        totens_esperados = listar_totem_id(1)
        self.assertEqual(data, totens_esperados)

    def test_listar_trancas_route(self):
        response = self.client.get('/tranca')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        trancas_esperaas = TrancaRepository().listar_trancas()
        self.assertEqual(data, trancas_esperaas)


    def test_listar_tranca_id_route(self):
        response = self.client.get('/tranca/1')
        data = response.text

        trancas_esperados = listar_tranca_id(1)
        self.assertEqual(data, trancas_esperados)

    
    ################################################################################
    #                                                                              #
    # o patch é usado para substituir a função chamada por um objeto de simulação  #
    # o objeto passado por parâmetro é um objeto "mock" para isolar o teste        #
    #                                                                              #
    ################################################################################


    @patch('service.BicicletaService.cadastrar_bicicleta')
    def test_cadastrar_bicicleta_route(self, mock_cadastrar_bicicleta):
        dados_cadastrados = {"id": "1", "marca": "marca_teste", "modelo": "modelo_teste", "ano": "2023", "numero": 1, "status": "DISPONIVEL"}
        mock_cadastrar_bicicleta.return_value = dados_cadastrados

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)
        response = self.client.post('/bicicleta', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, dados_cadastrados)


    @patch('service.TotemService.cadastrar_totem')
    def test_cadastrar_totem_route(self, mock_cadastrar_totem):
        dados_cadastrados = {"id": "1", "localizacao": "localizacao_teste", "modelo": "descricao_teste"}
        mock_cadastrar_totem.return_value = dados_cadastrados

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)
        response = self.client.post('/totem', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, dados_cadastrados)
    

    @patch('service.TrancaService.cadastrar_tranca')
    def test_cadastrar_tranca_route(self, mock_cadastrar_tranca):
        dados_cadastrados = {"id": "1", "numero": 1, "localizacao": "localizacao_teste", "ano_de_fabricacao": "2023", "modelo": "modelo_teste", "status": "DISPONIVEL"}
        mock_cadastrar_tranca.return_value = dados_cadastrados

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)
        response = self.client.post('/tranca', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, dados_cadastrados)


    @patch('service.BicicletaService.editar_bicicleta')
    def test_editar_bicicleta_route(self, mock_editar_bicicleta):
        dados_editados = {"id": "1", "marca": "marca_teste", "modelo": "modelo_teste", "ano": "2023", "numero": 1, "status": "DISPONIVEL"}
        mock_editar_bicicleta.return_value = dados_editados

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)
        response = self.client.put('/bicicleta/1', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=dados_editados)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, dados_editados)


    @patch('service.TotemService.editar_totem')
    def test_editar_totem_route(self, mock_editar_totem):
        dados_editados = {"id": "1", "localizacao": "localizacao_teste", "modelo": "descricao_teste"}
        mock_editar_totem.return_value = dados_editados

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)
        response = self.client.put('/totem/1', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=dados_editados)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, dados_editados)
    

    @patch('service.TrancaService.editar_tranca')
    def test_editar_tranca_route(self, mock_editar_tranca):
        dados_editados = {"id": "1", "numero": 1, "localizacao": "localizacao_teste", "ano_de_fabricacao": "2023", "modelo": "modelo_teste", "status": "DISPONIVEL"}
        mock_editar_tranca.return_value = dados_editados

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)
        response = self.client.put('/tranca/1', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=dados_editados)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, dados_editados)


    @patch('service.TrancaService.deletar_tranca')
    def test_deletar_tranca_invalido_route(self, mock_deletar_tranca):

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)

        response = self.client.delete('/tranca/1', headers={"Content-Type": "application/json", "X-CSRFToken": token})

        mock_deletar_tranca.return_value = "Dados não encontrados"


        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, mock_deletar_tranca.return_value)


    @patch('service.BicicletaService.deletar_bicicleta')
    def test_deletar_bicicleta_invalido_route(self, mock_deletar_bicicleta):

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)

        response = self.client.delete('/bicicleta/1', headers={"Content-Type": "application/json", "X-CSRFToken": token})

        mock_deletar_bicicleta.return_value = "Dados não encontrados"


        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, mock_deletar_bicicleta.return_value)


    @patch('service.TotemService.deletar_totem')
    def test_deletar_totem_invalido_route(self, mock_deletar_totem):

        response = self.client.get('/get_csrf_token')
        token = response.get_data(as_text=True)

        response = self.client.delete('/bicicleta/1', headers={"Content-Type": "application/json", "X-CSRFToken": token})

        mock_deletar_totem.return_value = "Dados não encontrados"


        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, mock_deletar_totem.return_value)

if __name__ == '__main__':
    unittest.main()