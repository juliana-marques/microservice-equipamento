import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root) 

class Bicicleta:
    def __init__(self, marca, modelo, ano, numero, status):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.numero = numero
        self.status = status