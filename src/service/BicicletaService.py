from unittest.mock import Mock
import os, sys

requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)     

from repository.bicicleta_repository import BicletaRepository

def listar_bicicletas():
    return BicletaRepository().listar_bicicleta()


def cadastrar_bicicleta(bicicleta):
    BicletaRepository().adicionar_bicicleta(bicicleta)
    

def editar_bicicleta(bicicleta_id, bicicleta):
    bicicletas = BicletaRepository().listar_bicicleta()
    
    for b in bicicletas:
        if b['id'] == bicicleta_id:
            bicicleta['id'] = bicicleta_id
            BicletaRepository().deletar_bicicleta(bicicleta_id)
            BicletaRepository().adicionar_bicicleta(bicicleta)
    return bicicleta
    

def deletar_bicicleta(bicicleta_id):
    return BicletaRepository().deletar_bicicleta(bicicleta_id)


def listar_bicicleta_id(bicicleta_id):
    bicicletas = BicletaRepository().listar_bicicleta()
    for b in bicicletas:
        if b['id'] == bicicleta_id:
            return b
    return "Não encontrado"