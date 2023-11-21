import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))                    
sys.path.insert(0, project_root)

bicicletas = []
id_bicicleta = 0

class BicletaRepository:
    def __init__(self):
        self.bicicletas = bicicletas


    def adicionar_bicicleta(self, bicicleta):
        global id_bicicleta
        print(bicicleta)
        try:   
            if bicicleta['id']:
                self.bicicletas.append(bicicleta)
        except:
            id_bicicleta += 1
            bicicleta['id'] = id_bicicleta
            self.bicicletas.append(bicicleta)
    

    def listar_bicicleta(self):
        return self.bicicletas
    

    def deletar_bicicleta(self, id_bicicleta):
        for bicicleta in self.bicicletas:
            if bicicleta['id'] == id_bicicleta:
                self.bicicletas.remove(bicicleta)
                return True
        return False