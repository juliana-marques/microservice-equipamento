class Bicicleta:
    
    def __init__(self, id=None, marca=None, modelo=None, ano=None, numero=None, status=None):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.numero = numero
        self.status = self.status_bicicleta(status)

    def status_bicicleta(self, status) :
        if status == 1:
            return "DISPONIVEL"
        elif status == 2:
            return "EM_USO"
        elif status == 3:
            return "NOVA"
        elif status == 4:
            return "APOSENTADA"
        elif status == 5:
            return "REPARO_SOLICITADO"
        elif status == 6:
            return "EM_REPARO"
        else:
            return None