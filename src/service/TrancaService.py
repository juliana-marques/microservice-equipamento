from unittest.mock import Mock
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)  

from repository.tranca_repository import TrancaRepository as repository

def listar_trancas():
    return repository().listar_trancas()

def cadastrar_tranca(tranca):
    repository().adicionar_tranca(tranca)

def editar_tranca(id_tranca, tranca):
    trancas = repository().listar_trancas()

    for t in trancas:
        if t['id'] == id_tranca:
            print(tranca)
            tranca['id'] = id_tranca
            repository().deletar_tranca(id_tranca)
            repository().adicionar_tranca(tranca)
    return tranca

def deletar_tranca(id_tranca):
    return repository().deletar_tranca(id_tranca)