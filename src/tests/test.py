import unittest, os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app
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

if __name__ == '__main__':
    unittest.main()