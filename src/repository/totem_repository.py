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
        
        return tranca
    
    def remover_tranca_totem(self, id_tranca, id_totem):
        for i, totem in enumerate(self.totens_tranca):
            if totem["id_totem"] == id_totem:
                trancas = totem["trancas"]

        for i, tranca in enumerate(trancas):
            if tranca["id"] == id_tranca:
                self.totens_tranca[i]["trancas"].remove(tranca)


    def integrar_bicicleta_tranca(self, tranca_adicionada):
        for i, totem in enumerate(self.totens_tranca):
            for j, tranca in enumerate(totem["trancas"]):
                if tranca["id"] == tranca_adicionada["id"]:
                    self.totens_tranca[i]["trancas"].remove(self.totens_tranca[i]["trancas"][j])
                    self.totens_tranca[i]["trancas"].append(tranca_adicionada)


    def retirar_bicicleta_tranca(self, tranca_removida):
        for i, totem in enumerate(self.totens_tranca):
            for j, tranca in enumerate(totem["trancas"]):
                if tranca["id"] == tranca_removida["id"]:
                    self.totens_tranca[i]["trancas"].remove(self.totens_tranca[i]["trancas"][j])
                    self.totens_tranca[i]["trancas"].append(tranca_removida)
                    