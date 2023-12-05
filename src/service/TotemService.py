from unittest.mock import Mock
import os, sys

requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)     

from repository.totem_repository import TotemRepository as repository
from model.totem import Totem

id_totem_global = 0

def listar_totens():
    return repository().listar_totens()


def cadastrar_totem(totem_dados):
    global id_totem_global
    id_totem_global += 1

    totem = Totem(
        id = id_totem_global,
        localizacao = totem_dados["localizacao"],
        descricao = totem_dados["descricao"]
    )

    totem_adicionar = {
        "id": totem.id,
        "localizacao": totem.localizacao,
        "descricao": totem.descricao
    }

    repository().adicionar_totem(totem_adicionar)

    return totem_adicionar


def deletar_totem(id_totem):
    return repository().deletar_totem(id_totem)


def listar_totem_id(totem_id):
    totens = repository().listar_totens()
    for totem in totens:
        if totem['id'] == totem_id:
            return totem
    return False

def adicionar_tranca_totem(id_totem, tranca, data):
    tranca = repository().adicionar_tranca_totem(id_totem, tranca, data)
    return tranca

def remover_tranca_totem(id_tranca, id_totem):
    repository().remover_tranca_totem(id_tranca, id_totem)

def listar_trancas_totem(id_totem):
    totens_tranca = repository().totens_tranca

    for totem in totens_tranca:
        if totem["id_totem"] == id_totem:
            return totem["trancas"]
    return []
        
def listar_bicicletas_totem(id_totem):
    totens_tranca = repository().totens_tranca
    bicicletas = []

    if len(totens_tranca) > 0:
        for totem in totens_tranca:
            if totem["id_totem"] == id_totem:
                trancas = totem["trancas"]

        if len(trancas) > 0:
            for tranca in trancas:
                if tranca["bicicleta"] != 0:
                    bicicletas.append(tranca["bicicleta"])

    return bicicletas
