import unittest, os, sys
from unittest.mock import patch
from flask_testing import TestCase

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app, enviar_email, verificar_funcionarios
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

        code = 200
        bicicletas_esperadas = listar_bicicleta_id(1)
        if bicicletas_esperadas == False:
            code = 404
            self.assertEqual("Dados não encontrados", response.text)

        self.assertEqual(response.status_code, code)


    def test_listar_totens_route(self):
        response = self.client.get('/totem')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        totens_esperados = TotemRepository().listar_totens()
        self.assertEqual(data, totens_esperados)


    def test_listar_totens_id_route_404(self):
        response = self.client.get('/totem/1')

        code = 200

        totens_esperados = listar_totem_id(1)
        if totens_esperados == False:
            code = 404
            self.assertEqual("Dados não encontrados", response.text)

        self.assertEqual(response.status_code, code)

    def test_listar_trancas_route(self):
        response = self.client.get('/tranca')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        trancas_esperaas = TrancaRepository().listar_trancas()
        self.assertEqual(data, trancas_esperaas)


    def test_listar_tranca_id_route(self):
        response = self.client.get('/tranca/1')

        code = 200
        trancas_esperados = listar_tranca_id(1)
        if trancas_esperados == False:
            code = 404
            self.assertEqual("Dados não encontrados", response.text)

        self.assertEqual(response.status_code, code)

    @patch('controller.main.cadastrar_bicicleta_route')
    def test_cadastrar_bicicleta_route_422(self, mock_cadastrar_bicicleta):
        dados_cadastrados = {"marca": "marca_teste", "modelo": "modelo_teste", "ano": "2023", "numero": 1, "status": 3}
        mock_cadastrar_bicicleta.return_value = dados_cadastrados

        response = self.client.post('/bicicleta', headers={"Content-Type": "application/json"}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 422)

    @patch('controller.main.cadastrar_bicicleta_route')
    def test_cadastrar_bicicleta_route_200(self, mock_cadastrar_bicicleta):
        dados_cadastrados = {"marca": "marca_teste", "modelo": "modelo_teste", "ano": "2023", "numero": 0, "status": 3}
        mock_cadastrar_bicicleta.return_value = dados_cadastrados

        response = self.client.post('/bicicleta', headers={"Content-Type": "application/json"}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 200)

    @patch('controller.main.cadastrar_totem_route')
    def test_cadastrar_bicicleta_routecadastrar_totem_route_422(self, mock_cadastrar_totem):
        dados_cadastrados = {"localizacao": "Localizacao_01"}
        mock_cadastrar_totem.return_value = dados_cadastrados

        response = self.client.post('/totem', headers={"Content-Type": "application/json"}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 422)

    @patch('controller.main.cadastrar_totem_route')
    def test_cadastrar_bicicleta_routecadastrar_totem_route_200(self, mock_cadastrar_totem):
        dados_cadastrados = {"localizacao": "Localizacao_01", "descricao": "teste"}
        mock_cadastrar_totem.return_value = dados_cadastrados

        response = self.client.post('/totem', headers={"Content-Type": "application/json"}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 200)


    @patch('controller.main.cadastrar_tranca_route')
    def test_cadastrar_tranca_routee_422(self, mock_cadastrar_tranca):
        dados_cadastrados = {"numero": 1, "localizacao": "modelo_teste", "ano_de_fabricacao": "2023", "modelo": 1, "status": 3}
        mock_cadastrar_tranca.return_value = dados_cadastrados

        response = self.client.post('/tranca', headers={"Content-Type": "application/json"}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 422)

    @patch('controller.main.cadastrar_tranca_route')
    def test_cadastrar_tranca_route_200(self, mock_cadastrar_tranca):
        dados_cadastrados = {"numero": 0, "localizacao": "modelo_teste", "ano_de_fabricacao": "2023", "modelo": "oi", "status": 1}
        mock_cadastrar_tranca.return_value = dados_cadastrados

        response = self.client.post('/tranca', headers={"Content-Type": "application/json"}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 200)

    @patch('controller.main.editar_tranca_route')
    def test_cadastrar_tranca_routee_404(self, mock_editar_tranca):
        dados_cadastrados = {"numero": 1, "localizacao": "modelo_teste", "ano_de_fabricacao": "2023", "modelo": 1, "status": 3}
        mock_editar_tranca.return_value = dados_cadastrados

        response = self.client.put('/tranca/1', headers={"Content-Type": "application/json"}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 422)

    @patch('controller.main.editar_tranca_route')
    def test_cadastrar_bicicleta_routee_404(self, mock_editar_bicicleta):
        dados_cadastrados = {"numero": 0, "localizacao": "modelo_teste", "ano_de_fabricacao": "2023", "modelo": 1, "status": 3}
        mock_editar_bicicleta.return_value = dados_cadastrados

        response = self.client.put('/bicicleta/1', headers={"Content-Type": "application/json"}, json=dados_cadastrados)

        self.assertEqual(response.status_code, 422)


    @patch('controller.main.enviar_email')
    def test_enviar_email_integration(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"status": "success"}

        resultado = enviar_email("Teste", "Isso é um teste")

        self.assertTrue(resultado)

    @patch('controller.main.verificar_funcionarios')
    def test_verificar_funcionarios_integration(self, mock_get):
        funcionarios_mock = {"funcionarios":[{"confirmacaoSenha":"123","cpf":"99999999999","email":"employee@example.com","funcao":"Reparador","id_funcionario":1,"idade":25,"matricula":"12345","nome":"Beltrano","senha":"123"}]}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = funcionarios_mock

        resultado = verificar_funcionarios(1)

        self.assertTrue(resultado)

    
    @patch('controller.main.verificar_funcionarios')
    def test_verificar_funcionarios_integration(self, mock_get):
        funcionarios_mock = {"funcionarios":[{"confirmacaoSenha":"123","cpf":"99999999999","email":"employee@example.com","funcao":"Reparador","id_funcionario":1,"idade":25,"matricula":"12345","nome":"Beltrano","senha":"123"}]}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = funcionarios_mock

        resultado = verificar_funcionarios(3)
        print(resultado)

        self.assertEqual(resultado[0], "Erro de integração")
        self.assertEqual(resultado[1], 404)    




if __name__ == '__main__':
    unittest.main()