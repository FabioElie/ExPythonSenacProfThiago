from Animal import Animal


class Gato(Animal):
    def __init__(self, nome, cor, raca):
        super().__init__(nome, cor)
        self.raca = raca

    def mover(self):
        return "O gato " + self.nome + " está pulando"

    def miar(self):
        return "O gato " + self.nome + " está miando MIAU"

    def info(self):
        return "Nome: " + self.nome + ", Cor: " + self.cor + ", Raça: " + self.raca
