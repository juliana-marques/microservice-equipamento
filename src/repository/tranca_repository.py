import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root) 

class TrancaRepository:
    def __init__(self):
        self.trancas = []


    def adicionar_tranca(self, tranca):
        self.trancas.append(tranca)
    
    
    def listar_trancas(self):
        return self.trancas
    

    def deletar_tranca(self, id_tranca):
        for tranca in self.trancas:
            if tranca['id'] == id_tranca:
                self.trancas.remove(tranca)
                return True
        return False