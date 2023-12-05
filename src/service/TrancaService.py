from unittest.mock import Mock
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)  

from repository.tranca_repository import TrancaRepository as repository
from repository.totem_repository import TotemRepository
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
        bicicleta=0,
        numero = numero_tranca_global,
        localizacao = tranca_dados["localizacao"],
        ano_de_fabricacao = tranca_dados["ano_de_fabricacao"],
        modelo = tranca_dados["modelo"],
        status = tranca_dados["status"]
    )

    tranca_adicionar = {
        "id": tranca.id,
        "bicicleta": tranca.bicicleta,
        "numero": tranca.numero,
        "localizacao": tranca.localizacao,
        "ano_de_fabricacao": tranca.ano_de_fabricacao,
        "modelo": tranca.modelo,
        "status": tranca.status,
    }

    repository().adicionar_tranca(tranca_adicionar)
    return tranca_adicionar

def editar_tranca(id_tranca, tranca_dados_editados):
    tranca = listar_tranca_id(id_tranca)

    tranca_editar = Tranca(
        id = id_tranca,
        bicicleta = tranca["bicicleta"],
        numero = tranca_dados_editados["numero"],
        localizacao = tranca_dados_editados["localizacao"],
        ano_de_fabricacao = tranca_dados_editados["ano_de_fabricacao"],
        modelo = tranca_dados_editados["modelo"],
        status = tranca_dados_editados["status"]
    )

    tranca_editada = {
        "id": tranca_editar.id,
        "bicicleta": tranca_editar.bicicleta,
        "numero": tranca_editar.numero,
        "localizacao": tranca_editar.localizacao,
        "ano_de_fabricacao": tranca_editar.ano_de_fabricacao,
        "modelo": tranca_editar.modelo,
        "status": tranca_editar.status,
    }

    if tranca["status"] != tranca_editada["status"]:
        return False
    
    repository().editar_tranca(tranca_editada)
    return tranca_editada

def deletar_tranca(id_tranca):
    return repository().deletar_tranca(id_tranca)


def integrar_tranca_rede(tranca):
    tranca_na_rede = Tranca(
        id = tranca["id"],
        bicicleta = tranca["bicicleta"],
        numero = tranca["numero"],
        localizacao = tranca["localizacao"],
        ano_de_fabricacao = tranca["ano_de_fabricacao"],
        modelo = tranca["modelo"],
        status = 5,
    )

    tranca_incluida = {
        "id": tranca_na_rede.id,
        "bicicleta": tranca_na_rede.bicicleta,
        "numero": tranca_na_rede.numero,
        "localizacao": tranca_na_rede.localizacao,
        "ano_de_fabricacao": tranca_na_rede.ano_de_fabricacao,
        "modelo": tranca_na_rede.modelo,
        "status": tranca_na_rede.status,
    }

    repository().editar_tranca(tranca_incluida)

    return tranca_incluida


def status_trancar(tranca):
    tranca_na_rede = Tranca(
        id = tranca["id"],
        bicicleta = tranca["bicicleta"],
        numero = tranca["numero"],
        localizacao = tranca["localizacao"],
        ano_de_fabricacao = tranca["ano_de_fabricacao"],
        modelo = tranca["modelo"],
        status = 3,
    )

    tranca_incluida = {
        "id": tranca_na_rede.id,
        "bicicleta": tranca_na_rede.bicicleta,
        "numero": tranca_na_rede.numero,
        "localizacao": tranca_na_rede.localizacao,
        "ano_de_fabricacao": tranca_na_rede.ano_de_fabricacao,
        "modelo": tranca_na_rede.modelo,
        "status": tranca_na_rede.status,
    }

    repository().editar_tranca(tranca_incluida)

    return tranca_incluida


def status_destrancar(tranca):
    tranca_na_rede = Tranca(
        id = tranca["id"],
        bicicleta = tranca["bicicleta"],
        numero = tranca["numero"],
        localizacao = tranca["localizacao"],
        ano_de_fabricacao = tranca["ano_de_fabricacao"],
        modelo = tranca["modelo"],
        status = 4,
    )

    tranca_incluida = {
        "id": tranca_na_rede.id,
        "bicicleta": tranca_na_rede.bicicleta,
        "numero": tranca_na_rede.numero,
        "localizacao": tranca_na_rede.localizacao,
        "ano_de_fabricacao": tranca_na_rede.ano_de_fabricacao,
        "modelo": tranca_na_rede.modelo,
        "status": tranca_na_rede.status,
    }

    repository().editar_tranca(tranca_incluida)

    return tranca_incluida

def integrar_bicicleta_tranca(tranca, bicicleta_numero):
    tranca_na_rede = Tranca(
        id = tranca["id"],
        bicicleta = bicicleta_numero,
        numero = tranca["numero"],
        localizacao = tranca["localizacao"],
        ano_de_fabricacao = tranca["ano_de_fabricacao"],
        modelo = tranca["modelo"],
        status = 3,
    )

    tranca_incluida = {
        "id": tranca_na_rede.id,
        "bicicleta": tranca_na_rede.bicicleta,
        "numero": tranca_na_rede.numero,
        "localizacao": tranca_na_rede.localizacao,
        "ano_de_fabricacao": tranca_na_rede.ano_de_fabricacao,
        "modelo": tranca_na_rede.modelo,
        "status": tranca_na_rede.status,
    }

    repository().editar_tranca(tranca_incluida)
    TotemRepository().integrar_bicicleta_tranca(tranca_incluida)

    return tranca_incluida

def tranca_alterar_status(tranca, acao):

    tranca_editar = Tranca(
        id = tranca["id"],
        bicicleta = tranca["bicicleta"],
        numero = tranca["numero"],
        localizacao = tranca["localizacao"],
        ano_de_fabricacao = tranca["ano_de_fabricacao"],
        modelo = tranca["modelo"],
        status = acao,
    )

    tranca_editada = {
        "id": tranca_editar.id,
        "bicicleta": tranca_editar.bicicleta,
        "numero": tranca_editar.numero,
        "localizacao": tranca_editar.localizacao,
        "ano_de_fabricacao": tranca_editar.ano_de_fabricacao,
        "modelo": tranca_editar.modelo,
        "status": tranca_editar.status,
    }

    repository().editar_tranca(tranca_editada)

    return tranca_editada

def retirar_bicicleta_rede(tranca):
    tranca_editar = Tranca(
        id = tranca["id"],
        bicicleta = 0,
        numero = tranca["numero"],
        localizacao = tranca["localizacao"],
        ano_de_fabricacao = tranca["ano_de_fabricacao"],
        modelo = tranca["modelo"],
        status = 2,
    )

    tranca_editada = {
        "id": tranca_editar.id,
        "bicicleta": tranca_editar.bicicleta,
        "numero": tranca_editar.numero,
        "localizacao": tranca_editar.localizacao,
        "ano_de_fabricacao": tranca_editar.ano_de_fabricacao,
        "modelo": tranca_editar.modelo,
        "status": tranca_editar.status,
    }
    
    repository().editar_tranca(tranca_editada)
    TotemRepository().retirar_bicicleta_tranca(tranca_editada)

    return tranca_editada

def retirar_tranca_rede(tranca, acao):
    tranca_editar = Tranca(
        id = tranca["id"],
        bicicleta = 0,
        numero = tranca["numero"],
        localizacao = tranca["localizacao"],
        ano_de_fabricacao = tranca["ano_de_fabricacao"],
        modelo = tranca["modelo"],
        status = acao,
    )

    tranca_editada = {
        "id": tranca_editar.id,
        "bicicleta": tranca_editar.bicicleta,
        "numero": tranca_editar.numero,
        "localizacao": tranca_editar.localizacao,
        "ano_de_fabricacao": tranca_editar.ano_de_fabricacao,
        "numero": tranca_editar.numero,
        "modelo": tranca_editar.modelo,
        "status": tranca_editar.status,
    }
    
    repository().editar_tranca(tranca_editada)

    return tranca_editada