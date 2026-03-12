# Classe Transporte: Crie uma super classe Transporte e suas respectivas subclasses, 
# sendo Terrestre e uma terceira subclasse de transporte Automóvel

class Transporte:
    def __init__(self, marca: str, modelo: str, capacidade: int):
        self.marca = marca
        self.modelo = modelo
        self.capacidade = capacidade

    def viajar(self, destino: str) -> None:
        print(f"{self.modelo} da {self.marca} viajando para {destino}.")


class Aquatico(Transporte):
    def navegar(self) -> None:
        print(f"{self.modelo} está navegando nas águas.")

class Aereo(Transporte):
    def voar(self) -> None:
        print(f"{self.modelo} está voando pelos ares.")

class Terrestre(Transporte):
    def dirigir(self) -> None:
        print(f"{self.modelo} está dirigindo na estrada.")


class Carro(Terrestre):
    def __init__(self, marca: str, modelo: str, capacidade: int, portas: int):
        super().__init__(marca, modelo, capacidade)
        self.portas = portas

    def abrir_porta(self) -> None:
        print(f"Abrindo porta do carro {self.modelo}.")


class Moto(Terrestre):
    def __init__(self, marca: str, modelo: str, capacidade: int, cilindradas: int):
        super().__init__(marca, modelo, capacidade)
        self.cilindradas = cilindradas

    def empinar(self) -> None:
        print(f"Moto {self.modelo} empinando!")

print("-" * 40)
barco = Aquatico("Yamaha", "Barco X", 8)
barco.viajar("Ilha")
barco.navegar()
print("-" * 40)
carro = Carro("Fiat", "Uno", 5, portas=4)
carro.viajar("São Paulo")
carro.dirigir()
carro.abrir_porta()
print("-" * 40)
moto = Moto("Honda", "CBR", 2, cilindradas=600)
moto.viajar("Campinas")
moto.dirigir()
moto.empinar()
print("-" * 40)
aviao = Aereo("Boeing", "747", 660)
aviao.viajar("Nova York")
aviao.voar()
