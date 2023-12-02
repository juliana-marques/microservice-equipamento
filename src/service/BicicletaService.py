from unittest.mock import Mock
import os, sys

requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)     

from repository.bicicleta_repository import BicletaRepository
from model.bicicleta import Bicicleta
id_bicicleta_global = 0
numero_bicicleta_global = 0

def listar_bicicletas():
    return BicletaRepository().listar_bicicleta()


def listar_bicicleta_id(bicicleta_id):
    bicicletas = BicletaRepository().listar_bicicleta()
    for bicicleta in bicicletas:
        if bicicleta['id'] == bicicleta_id:
            return bicicleta
    return False


def cadastrar_bicicleta(bicicleta_dados):
    global id_bicicleta_global
    global numero_bicicleta_global
    id_bicicleta_global += 1
    numero_bicicleta_global += 1

    bicicleta = Bicicleta(
        id = id_bicicleta_global,
        marca = bicicleta_dados["marca"],
        modelo = bicicleta_dados["modelo"],
        ano = bicicleta_dados["ano"],
        numero = numero_bicicleta_global,
        status = bicicleta_dados["status"],
    )

    bicicleta_adicionar = {
        "id": bicicleta.id,
        "marca": bicicleta.marca,
        "modelo": bicicleta.modelo,
        "ano": bicicleta.ano,
        "numero": bicicleta.numero,
        "status": bicicleta.status
    }

    BicletaRepository().adicionar_bicicleta(bicicleta_adicionar)
    return bicicleta_adicionar
    

def editar_bicicleta(bicicleta_id, bicicleta_dados_editados):

    bicicleta = listar_bicicleta_id(bicicleta_id)
    if bicicleta["numero"] != bicicleta_dados_editados["numero"]:
        return False
    
    bicicleta_editar = Bicicleta(
        id = bicicleta_id,
        marca = bicicleta_dados_editados["marca"],
        modelo = bicicleta_dados_editados["modelo"],
        ano = bicicleta_dados_editados["ano"],
        numero = bicicleta_dados_editados["numero"],
        status = bicicleta_dados_editados["status"],
    )

    bicicleta_editada = {
        "id": bicicleta_editar.id,
        "marca": bicicleta_editar.marca,
        "modelo": bicicleta_editar.modelo,
        "ano": bicicleta_editar.ano,
        "numero": bicicleta_editar.numero,
        "status": bicicleta_editar.status
    }

    if bicicleta["status"] != bicicleta_editada["status"]:
        return False
    
    BicletaRepository().editar_bicicleta(bicicleta_editada)

    return bicicleta_editada
    

def deletar_bicicleta(bicicleta_id):
    return BicletaRepository().deletar_bicicleta(bicicleta_id)


def integrar_bicicleta_rede(data):
    bicicletas = BicletaRepository().listar_bicicleta()
    for b in bicicletas:
        if b['numero'] == data and (b['status'] == "NOVA" or b['status'] == "EM_REPARO"):
            b['status'] = "DISPONIVEL"
            editar_bicicleta(b['id'], b)
            return True
    return False

def retirar_bicicleta_rede(data):
    bicicletas = BicletaRepository().listar_bicicleta()

    if data['status_acao_reparador'] == "REPARO":
        for bicicleta in bicicletas:
            if data['numero_bicicleta'] == bicicleta['numero'] and bicicleta['status'] == "REPARO_SOLICITADO":
                bicicleta['status'] = "EM_REPARO"
                editar_bicicleta(bicicleta['id'], bicicleta)
                # envia email / registra data  e hota, numero e o reparador
                return True
            
    elif data['status_acao_reparador'] == "APOSENTADORIA":
        for bicicleta in bicicletas:
            if data['numero_bicicleta'] == bicicleta['numero'] and bicicleta['status'] == "REPARO_SOLICITADO":
                bicicleta['status'] = "APOSENTADA"
                editar_bicicleta(bicicleta['id'], bicicleta)
                # envia email / registra data  e hota, numero e o reparador
                return True
    return False

def enum_status(acao):
    if acao == 1:
        return "DISPONIVEL"
    elif acao == 2:
        return "EM_USO"
    elif acao == 3:
        return "NOVA"
    elif acao == 4:
        return "APOSENTADA"
    elif acao == 5:
        return "REPARO_SOLICITADO"
    elif acao == 6:
        return "EM_REPARO"

def status_bicicleta(bicicleta_id, acao):
    bicicletas = BicletaRepository().listar_bicicleta()
    for b in bicicletas:
        if b['id'] == bicicleta_id:
            status = enum_status(acao)
            b['status'] = status
            editar_bicicleta(b['id'], b)
            return True
    return False
