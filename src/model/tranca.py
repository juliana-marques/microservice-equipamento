class Tranca:
    
    def __init__(self, id=None, bicicleta=0, numero=None, localizacao=None, ano_de_fabricacao=None, modelo=None, status=None):
        self.id = id
        self.bicicleta = bicicleta
        self.numero = numero
        self.localizacao = localizacao
        self.ano_de_fabricacao = ano_de_fabricacao
        self.modelo = modelo
        self.status = self.status_tranca(status)

    def status_tranca(self, status) :
        if status == 1:
            return "NOVA"
        elif status == 2:
            return "DESTRANCAR"
        elif status == 3:
            return "TRANCAR"
        elif status == 4:
            return "EM_REPARO"
        elif status == 5:
            return "DISPONIVEL"
        elif status == 6:
            return "LIVRE"
        elif status == 7:
            return "APOSENTADA"
        elif status == 8:
            return "REPARO_SOLICITADO"
        else:
            return None