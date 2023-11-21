bicicletas = []
id_bicicleta_global = 0

class BicletaRepository:
    def __init__(self):
        self.bicicletas = bicicletas


    def adicionar_bicicleta(self, bicicleta):
        global id_bicicleta_global
        try:   
            if bicicleta['id']:
                self.bicicletas.append(bicicleta)
        except Exception as e:
            id_bicicleta_global += 1
            bicicleta['id'] = id_bicicleta_global
            self.bicicletas.append(bicicleta)
            print(e)
    

    def listar_bicicleta(self):
        return self.bicicletas
    

    def deletar_bicicleta(self, id_bicicleta):
        for bicicleta in self.bicicletas:
            if bicicleta['id'] == id_bicicleta:
                self.bicicletas.remove(bicicleta)
                return True
        return False