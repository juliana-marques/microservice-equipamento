trancas = []
id_tranca_global = 0

class TrancaRepository:
    def __init__(self):
        self.trancas = trancas


    def adicionar_tranca(self, tranca):
        global id_tranca_global
        try:   
            if tranca['id']:
                self.trancas.append(tranca)
        except Exception as e:
            id_tranca_global += 1
            tranca['id'] = id_tranca_global
            self.trancas.append(tranca)
            print(e)
    

    def listar_trancas(self):
        return self.trancas
    

    def deletar_tranca(self, id_tranca):
        for tranca in self.trancas:
            if tranca['id'] == id_tranca:
                self.trancas.remove(tranca)
                return True
        return False