from Animal import Animal


class Peixe(Animal):
    def __init__(self, nome, cor, tipo):
        super().__init__(nome, cor)
        self.tipo = tipo

    def mover(self):
        return "O peixe " + self.nome + " está nadando"

    def fazGluGlu(self):
        return "O peixe " + self.nome + " está fazendo GLU GLU IE IÉ"

    def info(self):
        return "Nome: " + self.nome + ", Cor: " + self.cor + ", Tipo: " + self.tipo
