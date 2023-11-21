import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root) 

class Totem:
    def __init__(self, localizacao, descricao):
        self.localizacao = localizacao
        self.descricao = descricao
