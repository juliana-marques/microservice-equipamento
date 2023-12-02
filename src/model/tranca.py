class Tranca:
    
    def __init__(self, id=None, numero=None, localizacao=None, ano_de_fabricacao=None, modelo=None, status=None):
        self.id = id
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
        else:
            return None