bicicletas = []

class BicletaRepository:
    def __init__(self):
        self.bicicletas = bicicletas


    def adicionar_bicicleta(self, bicicleta):
        self.bicicletas.append(bicicleta)
        

    def listar_bicicleta(self):
        return self.bicicletas
    

    def deletar_bicicleta(self, id_bicicleta):
        for bicicleta in self.bicicletas:
            if bicicleta['id'] == id_bicicleta:
                self.bicicletas.remove(bicicleta)
                return True
        return False
    
    def editar_bicicleta(self, bicicleta_editada):
        bicicletas = self.listar_bicicleta()

        for bicicleta in bicicletas:
            if bicicleta["id"] == bicicleta_editada["id"]:
                self.bicicletas.remove(bicicleta)
                self.bicicletas.append(bicicleta_editada)