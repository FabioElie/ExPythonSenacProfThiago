# 10 - Classe Carro: Crie uma classe que modele um Livro. Esta classe deve possuir os seguintes 
# atributos:
#  Modelo, Marca, Cor, Ano, Valor, Nível (default 0) , Consumo
#  A classe deve ter o seguintes métodos:
#  abastecer(); - deve incrementar no nível do tanque de combustível.
#  andar(); - recebe a distancia em km que o veículo andou
#  verificar_nível(); - o deve criar uma forma de calcular quantos litros de comb. foram gasto por km
#  calcular_imposto()  -  deve considerar o IPVA do carro em 2,5% do valor.

class Carro:
    def __init__(
        self,
        modelo: str,
        marca: str,
        cor: str,
        ano: int,
        valor: float,
        consumo: float,
        nivel: float = 0.0,
    ):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo  
        self.nivel = nivel 
        self.consumo_total = 0.0
        self.distancia_total = 0.0

    def abastecer(self, litros: float) -> None:
        if litros > 0:
            self.nivel += litros
        else:
            print("Quantidade de litros deve ser positiva.")

    def andar(self, km: float) -> None:
        if km <= 0:
            print("Distância deve ser positiva.")
            return
        gasto = km * self.consumo
        if gasto > self.nivel:
            print("Tanque insuficiente para essa distância.")
            return
        self.nivel -= gasto
        self.consumo_total += gasto
        self.distancia_total += km

    def verificar_nivel(self) -> float:
        if self.distancia_total == 0:
            return 0.0
        return self.consumo_total / self.distancia_total

    def calcular_imposto(self) -> float:
        return self.valor * 0.025




carro1 = Carro("Uno", "Fiat", "Prata", 2010, 25000.0, consumo=0.1)
carro1.abastecer(40)
carro1.andar(200)
print(f"\nCarro: {carro1.modelo} {carro1.marca}")
print(f"Nível do tanque: {carro1.nivel:.2f}l")
print(f"Média consumo: {carro1.verificar_nivel():.3f} l/km")
print(f"IPVA: R$ {carro1.calcular_imposto():.2f}")

carro2 = Carro("Civic", "Honda", "Preto", 2022, 100000.0, consumo=0.08)
carro2.abastecer(50)
carro2.andar(400)
print(f"\nCarro: {carro2.modelo} {carro2.marca}")
print(f"Nível do tanque: {carro2.nivel:.2f}l")
print(f"Média consumo: {carro2.verificar_nivel():.3f} l/km")
print(f"IPVA: R$ {carro2.calcular_imposto():.2f}")

