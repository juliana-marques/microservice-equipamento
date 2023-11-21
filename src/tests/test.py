import unittest, os, sys, json
from unittest.mock import Mock, patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app
from repository.bicicleta_repository import BicletaRepository
from repository.totem_repository import TotemRepository
from repository.tranca_repository import TrancaRepository
from service.BicicletaService import listar_bicicletas, cadastrar_bicicleta, editar_bicicleta, deletar_bicicleta, listar_bicicleta_id, integrar_bicicleta_rede, retirar_bicicleta_rede


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

    def test_listar_totens_route(self):
        response = self.client.get('/totem')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        totens_esperados = TotemRepository().listar_totens()
        self.assertEqual(data, totens_esperados)

    def test_listar_trancas_route(self):
        response = self.client.get('/tranca')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        trancas_esperaas = TrancaRepository().listar_trancas()
        self.assertEqual(data, trancas_esperaas)

    
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

if __name__ == '__main__':
    unittest.main()