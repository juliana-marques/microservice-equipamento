import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root) 

class Tranca:
    def __init__(self, numero, localizacao, ano_de_fabricacao, modelo, status):
        self.numero = numero
        self.localizacao = localizacao
        self.ano_de_fabricacao = ano_de_fabricacao
        self.modelo = modelo
        self.status = status