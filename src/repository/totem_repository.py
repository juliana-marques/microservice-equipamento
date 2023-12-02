totens = []
totens_tranca = []


class TotemRepository:
    def __init__(self):
        self.totens = totens
        self.totens_tranca = totens_tranca


    def adicionar_totem(self, totem):
        self.totens.append(totem)
    

    def listar_totens(self):
        return self.totens
    

    def deletar_totem(self, id_totem):
        for totem in self.totens:
            if totem['id'] == id_totem:
                self.totens.remove(totem)
                return True
        return False

    
    def listar_trancas_totem(self, id_totem):
        for totem in totens_tranca:
            if totem["id_totem"] == id_totem:
                return totem["trancas"]
        return False
    
    def criar_totem_listagem(self, id_totem, tranca):

        data = {
            "id_totem": id_totem,
            "trancas": [
                tranca
            ]
        }

        self.totens_tranca.append(data)
        
        return data

    def adicionar_tranca_totem(self, id_totem, tranca, data_integracao):
        result = self.listar_trancas_totem(id_totem)

        tranca["data_integracao"] = data_integracao
        if result == False:
            data = self.criar_totem_listagem(id_totem, tranca)
            return data
        
        for i, totem in enumerate(self.totens_tranca):
            if totem["id_totem"] == id_totem:
                self.totens_tranca[i]["trancas"].append(tranca)
        
        print(self.totens_tranca)
        return tranca