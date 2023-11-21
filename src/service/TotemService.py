from unittest.mock import Mock
import os, sys

requests = Mock()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)     

from repository.totem_repository import TotemRepository as repository
 

def listar_totens():
    return repository().listar_totens()


def cadastrar_totem(totem):
    repository().adicionar_totem(totem)

def editar_totem(id_totem, totem):
    totens = repository().listar_totens()

    for t in totens:
        if t['id'] == id_totem:
            totem['id'] = id_totem
            repository().deletar_totem(id_totem)
            repository().adicionar_totem(totem)
    return totem


def deletar_totem(id_totem):
    return repository().deletar_totem(id_totem)