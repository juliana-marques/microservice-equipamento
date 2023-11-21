class BicletaRepository:
    def __init__(self):
        self.bicicletas = []


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