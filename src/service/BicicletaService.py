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

def integrar_bicicleta_rede(data):
    bicicletas = BicletaRepository().listar_bicicleta()
    for b in bicicletas:
        if b['numero'] == data:
            b['status'] = "DISPONIVEL"
            editar_bicicleta(b['id'], b)
            return True
    return False

def retirar_bicicleta_rede(data):
    bicicletas = BicletaRepository().listar_bicicleta()

    if data['status_acao_reparador'] == "REPARO":
        for bicicleta in bicicletas:
            if data['numero_bicicleta'] == bicicleta['numero']:
                bicicleta['status'] = "EM_REPARO"
                editar_bicicleta(bicicleta['id'], bicicleta)
                # envia email / registra data  e hota, numero e o reparador
                return True
            
    elif data['status_acao_reparador'] == "APOSENTADORIA":
        for bicicleta in bicicletas:
            if data['numero_bicicleta'] == bicicleta['numero']:
                bicicleta['status'] = "APOSENTADA"
                editar_bicicleta(bicicleta['id'], bicicleta)
                # envia email / registra data  e hota, numero e o reparador
                return True
    return False
