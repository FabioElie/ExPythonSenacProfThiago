from Animal import Animal


class Cachorro(Animal):
    def __init__(self, nome, cor, raca, rabo=True):
        super().__init__(nome, cor)
        self.raca = raca
        self.rabo = rabo

    def mover(self):
        return "O cachorro " + self.nome + " está correndo"

    def latir(self):
        return "O cachorro " + self.nome + " está latindo AUAUAU"

    def info(self):
        return (
            "Nome: "
            + self.nome
            + ", Cor: "
            + self.cor
            + ", Raça: "
            + self.raca
            + ", Tem rabo: "
            + str(self.rabo)
        )
