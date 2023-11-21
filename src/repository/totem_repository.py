import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root) 

class TotemRepository:
    def __init__(self):
        self.totens = []


    def adicionar_totem(self, totem):
        self.totens.append(totem)
        return totem
    

    def listar_totens(self):
        return self.totens
    
    
    def deletar_totem(self, id_totem):
        for totem in self.totens:
            if totem['id'] == id_totem:
                self.totens.remove(totem)
                return True
        return False