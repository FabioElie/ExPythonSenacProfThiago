class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def mover(self):
        return "O Animal genérico " + self.nome + " se moveu"

    def fazerSom(self):
        return "O Animal genérico " + self.nome + " fez algum som muito louco"

    def info(self):
        return "Nome: " + self.nome + ", Cor: " + self.cor
