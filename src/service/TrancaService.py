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
            tranca['id'] = id_tranca
            repository().deletar_tranca(id_tranca)
            repository().adicionar_tranca(tranca)
    return tranca

def deletar_tranca(id_tranca):
    return repository().deletar_tranca(id_tranca)

def listar_tranca_id(tranca_id):
    trancas = repository().listar_trancas()
    for t in trancas:
        if t['id'] == tranca_id:
            return t
    return "Não encontrado"

def integrar_tranca_rede(numero_tranca):
    trancas = repository().listar_trancas()
    
    for tranca in trancas:
        if numero_tranca['numero'] == tranca['numero']:
            if tranca['status'] == "NOVA" or tranca['status'] == "EM_REPARO":
                tranca['status'] = "DISPONIVEL"
                tranca = editar_tranca(tranca['id'], tranca)
                # enviar email
                # se em reparo -> conferir funcionário
                # inserir data e hora na inserção do totem, matricula do reparador e o numero da tranca
                return True
    return False

def retirar_tranca_rede(numero_tranca):
    trancas = listar_trancas
    
    for tranca in trancas:
        if numero_tranca == tranca['numero']:
            if tranca['status'] == "NOVA" or tranca['status'] == "EM_REPARO":
                tranca['status'] = "DISPONIVEL"
                tranca = editar_tranca(tranca['id'], tranca)
                return True
    return False