# 7 - Classe Brinquedos: Andy Davis precisa classificar seus brinquedos por Subclasses, 
# sabemos que cada brinquedo tem atributos e métodos diferentes, exemplo Buzz Lightyear 
# voa e Woody laça. Defina principais atributos:
#  Nome, Cor, Tamanho, Preço;
#  Método:
#  brincar(); - fazer um print simples, estou brincando com {nome do brinquedo}
#  Subclasses:
#  Crie 10 sub classes de brinquedos com seus respectivos atributos e métodos.
#  Utilize o polimorfismo para reescrever o método herdado da super classe


class Brinquedo:
    def __init__(self, nome: str, cor: str, tamanho: str, preco: float):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self) -> None:
        print(f"Estou brincando com {self.nome}.")


class BuzzLightyear(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float):
        super().__init__("Buzz Lightyear", cor, tamanho, preco)

    def voar(self) -> None:
        print("Buzz está voando pelo espaço!")

    def brincar(self) -> None:
        print(f"{self.nome}: " + "Prepare-se para decolar!")


class Woody(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float):
        super().__init__("Woody", cor, tamanho, preco)

    def lacar(self) -> None:
        print("Woody está laçando um inimigo.")

    def brincar(self) -> None:
        print(f"{self.nome}: " + "Vamos ser heróis do brinquedo!")


class Carro(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float):
        super().__init__("Carro", cor, tamanho, preco)

    def acelerar(self) -> None:
        print(f"{self.nome} acelera a toda velocidade!")

    def brincar(self) -> None:
        print(f"{self.nome}: corrida iniciada!")


class Boneca(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float):
        super().__init__("Boneca", cor, tamanho, preco)

    def vestir(self, roupa: str) -> None:
        print(f"{self.nome} foi vestida com {roupa}.")

    def brincar(self) -> None:
        print(f"{self.nome}: brincando de casinha.")


class Robo(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float, energia: int):
        super().__init__("Robô", cor, tamanho, preco)
        self.energia = energia

    def carregar(self) -> None:
        self.energia = 100
        print("Robô carregado até 100 de energia.")

    def brincar(self) -> None:
        print(f"{self.nome}: enfrentando os Power Rangers.")


class Ursinho(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float):
        super().__init__("Ursinho", cor, tamanho, preco)

    def abraçar(self) -> None:
        print(f"{self.nome} dá um abraço quentinho.")

    def brincar(self) -> None:
        print(f"{self.nome}: hora do cochilo!")


class Bola(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float):
        super().__init__("Bola", cor, tamanho, preco)

    def quicar(self) -> None:
        print(f"A bola {self.nome} quica alto!")

    def brincar(self) -> None:
        print(f"{self.nome}: jogo de futebol começando!")


class QuebraCabeca(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float, pecas: int):
        super().__init__("Quebra-Cabeça", cor, tamanho, preco)
        self.pecas = pecas

    def brincar(self) -> None:
        print(f"Montando o quebra-cabeça de {self.pecas} peças.")


class Lego(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float, pecas: int):
        super().__init__("Lego", cor, tamanho, preco)
        self.pecas = pecas

    def construir(self, modelo: str) -> None:
        print(f"Construindo um {modelo} com Lego.")

    def brincar(self) -> None:
        print(f"{self.nome}: criatividade em ação.")


class Pelucia(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float):
        super().__init__("Pelúcia", cor, tamanho, preco)

    def acalmar(self) -> None:
        print(f"Pelúcia {self.nome} acalma a criança.")

    def brincar(self) -> None:
        print(f"{self.nome}: hora do aconchego.")


class Drone(Brinquedo):
    def __init__(self, cor: str, tamanho: str, preco: float):
        super().__init__("Drone", cor, tamanho, preco)

    def voar(self) -> None:
        print("Drone voando nos céus.")

    def brincar(self) -> None:
        print(f"{self.nome}: pilotando acima das nuvens.")


brinquedos = [
    BuzzLightyear("branco e verde", "médio", 150.0),
    Woody("marrom", "médio", 120.0),
    Carro("vermelho", "pequeno", 50.0),
    Boneca("rosa", "pequeno", 70.0),
    Robo("prata", "médio", 200.0, energia=80),
    Ursinho("marrom", "pequeno", 60.0),
    Bola("colorida", "médio", 30.0),
    QuebraCabeca("multicolor", "grande", 90.0, pecas=500),
    Lego("multicolor", "grande", 120.0, pecas=1000),
    Pelucia("branco", "pequeno", 40.0),
    Drone("branco", "pequeno", 250.0),
]

for b in brinquedos:
    b.brincar()
