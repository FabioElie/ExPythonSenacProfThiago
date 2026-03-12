# 1 - Classe Filme: Crie uma super classe que modele um Filme. Esta classe deve possuir os 
# seguintes atributos:
#  Nome;
#  Duração;
#  Método:
#  Play(): deve exibir que foi dado play no filme;
#  Subclasses:
#  Defina as subclasses de Filme, exemplo Ação, Drama e Suspense. Após a criação das subclasses 
# você deve criar novos métodos específicos a cada subclasse, ex: explodir() em Ação

class Filme:
    def __init__(self, nome: str, duracao: float):
        self.nome = nome
        self.duracao = duracao

    def play(self) -> None:
        print(f"Play no filme {self.nome} de duração {self.duracao} minutos.")


class Acao(Filme):
    def explodir(self) -> None:
        print(f"{self.nome}: explosão em 3... 2... 1!")


class Drama(Filme):
    def chorar(self) -> None:
        print(f"{self.nome}: hora de chorar.")


class Suspense(Filme):
    def gritar(self) -> None:
        print(f"{self.nome}: Jumpscare.. AAAHHHH!")


filme1 = Acao("Velozes e Furiosos", 130)
filme1.play()
filme1.explodir()

filme2 = Drama("Titanic", 195)
filme2.play()
filme2.chorar()

filme3 = Suspense("Invocação do Mal", 110)
filme3.play()
filme3.gritar()