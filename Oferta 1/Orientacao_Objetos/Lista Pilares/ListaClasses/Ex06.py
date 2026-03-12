# 6 - Classe Círculo: crie uma classe que represente um círculo. Esta classe deve possuir o 
# seguinte atributo:
#  raio
#  A classe deve ter os seguintes métodos:
#  imprimir o valor do raio;
#  calcular a área do círculo;
#  calcular a circunferência do círculo

import math

class Circulo:
    def __init__(self, raio: float):
        self.raio = raio

    def imprimir_raio(self) -> None:
        print(f"Raio: {self.raio}")

    def calcular_area(self) -> float:
        return math.pi * (self.raio ** 2)

    def calcular_circunferencia(self) -> float:
        return 2 * math.pi * self.raio



circulo1 = Circulo(5)
circulo1.imprimir_raio()
print(f"Área: {circulo1.calcular_area():.2f}")
print(f"Circunferência: {circulo1.calcular_circunferencia():.2f}")
