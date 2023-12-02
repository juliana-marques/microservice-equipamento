trancas = []

class TrancaRepository:
    def __init__(self):
        self.trancas = trancas


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
    
    def editar_tranca(self, tranca_editada):
        trancas = self.listar_trancas()

        for tranca in trancas:
            if tranca["id"] == tranca_editada["id"]:
                self.trancas.remove(tranca)
                self.trancas.append(tranca_editada)