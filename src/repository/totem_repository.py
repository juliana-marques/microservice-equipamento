totens = []
id_totem_global = 0

class TotemRepository:
    def __init__(self):
        self.totens = totens


    def adicionar_totem(self, totem):
        global id_totem_global
        try:   
            if totem['id']:
                self.totens.append(totem)
        except:
            id_totem_global += 1
            totem['id'] = id_totem_global
            self.totens.append(totem)
    

    def listar_totens(self):
        return self.totens
    

    def deletar_totem(self, id_totem):
        for totem in self.totens:
            if totem['id'] == id_totem:
                self.totens.remove(totem)
                return True
        return False