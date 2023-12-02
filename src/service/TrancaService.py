from unittest.mock import Mock
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)  

from repository.tranca_repository import TrancaRepository as repository
from model.tranca import Tranca

id_tranca_global = 0
numero_tranca_global = 0

def listar_trancas():
    return repository().listar_trancas()


def listar_tranca_id(tranca_id):
    trancas = repository().listar_trancas()
    for tranca in trancas:
        if tranca['id'] == tranca_id:
            return tranca
    return False


def cadastrar_tranca(tranca_dados):
    global id_tranca_global
    global numero_tranca_global
    id_tranca_global += 1
    numero_tranca_global += 1

    tranca = Tranca(
        id = id_tranca_global,
        numero = numero_tranca_global,
        localizacao = tranca_dados["localizacao"],
        ano_de_fabricacao = tranca_dados["ano_de_fabricacao"],
        modelo = tranca_dados["modelo"],
        status = tranca_dados["status"]
    )

    tranca_adicionar = {
        "id": tranca.id,
        "numero": tranca.numero,
        "localizacao": tranca.localizacao,
        "ano_de_fabricacao": tranca.ano_de_fabricacao,
        "numero": tranca.numero,
        "modelo": tranca.modelo,
        "status": tranca.status,
    }

    repository().adicionar_tranca(tranca_adicionar)
    return tranca_adicionar

def editar_tranca(id_tranca, tranca_dados_editados):
    tranca = listar_tranca_id(id_tranca)

    tranca_editar = Tranca(
        id = id_tranca,
        numero = tranca_dados_editados["numero"],
        localizacao = tranca_dados_editados["localizacao"],
        ano_de_fabricacao = tranca_dados_editados["ano_de_fabricacao"],
        modelo = tranca_dados_editados["modelo"],
        status = tranca_dados_editados["status"]
    )

    tranca_editada = {
        "id": tranca_editar.id,
        "numero": tranca_editar.numero,
        "localizacao": tranca_editar.localizacao,
        "ano_de_fabricacao": tranca_editar.ano_de_fabricacao,
        "numero": tranca_editar.numero,
        "modelo": tranca_editar.modelo,
        "status": tranca_editar.status,
    }

    if tranca["status"] != tranca_editada["status"]:
        return False
    return tranca_editada

def deletar_tranca(id_tranca):
    return repository().deletar_tranca(id_tranca)


def integrar_tranca_rede(data):
    trancas = repository().listar_trancas()
    
    for tranca in trancas:
        if data['numero'] == tranca['numero']:
            if tranca['status'] == "NOVA" or tranca['status'] == "EM_REPARO":
                tranca['status'] = "DISPONIVEL"
                tranca = editar_tranca(tranca['id'], tranca)
                # enviar email
                # se em reparo -> conferir funcionário
                # inserir data e hora na inserção do totem, matricula do reparador e o numero da tranca
                return True
    return False

def retirar_tranca_rede(data):
    trancas = repository().listar_trancas()

    if data['status_acao_reparador'] == "REPARO":
        for tranca in trancas:
            if data['numero'] == tranca['numero'] and tranca['status'] != "DESTRANCAR":
                tranca['status'] = "EM_REPARO"
                tranca = editar_tranca(tranca['id'], tranca)
                # envia email / registra data  e hota, numero e o reparador
                return True
            
    elif data['status_acao_reparador'] == "APOSENTADORIA":
        for tranca in trancas:
            if data['numero'] == tranca['numero']:
                tranca['status'] = "APOSENTADA"
                tranca = editar_tranca(tranca['id'], tranca)
                # envia email / registra data  e hota, numero e o reparador
                return True
    return False

def validar_tranca_integrar_bicicleta(data):
    trancas = repository().listar_trancas()
    for tranca in trancas:
        if data == tranca['id'] and tranca['status'] == "DISPONIVEL":
            return True
    return False

def fechamento_da_tranca(data):
    trancas = repository().listar_trancas()
    for tranca in trancas:
        if data == tranca['numero']:
            tranca['status'] = "EM_USO"
            tranca = editar_tranca(tranca['id'], tranca)
            return True
    return False

def validar_tranca_retirar_bicicleta(data):
    trancas = repository().listar_trancas()
    for tranca in trancas:
        if data['numero_tranca'] == tranca['numero']:
            tranca['status'] = "DESTRANCAR"
            tranca = editar_tranca(tranca['id'], tranca)
            return True
    return False

def trancar(id_tranca):
    trancas = repository().listar_trancas()
    for tranca in trancas:
        if id_tranca == tranca['id']:
            tranca['status'] = "TRANCAR"
            tranca = editar_tranca(tranca['id'], tranca)
            return True
        return False

def destrancar(id_tranca):
    trancas = repository().listar_trancas()
    for tranca in trancas:
        if id_tranca == tranca['id']:
            tranca['status'] = "DESTRANCAR"
            tranca = editar_tranca(tranca['id'], tranca)
            return True
        return False