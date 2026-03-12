# 8 - Classe Triangulo: Crie uma classe que modele um triangulo: – Atributos: LadoA, LadoB, LadoC– Métodos: calcular Perímetro, getMaiorLado; 
#  Crie instâncias desta classe. Ele deve pedir ao usuário que informe as medidas de um 
# triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado

import math

class Triangulo:
    def __init__(self, ladoA: float, ladoB: float, ladoC: float):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self) -> float:
        return self.ladoA + self.ladoB + self.ladoC

    def get_maior_lado(self) -> float:
        return max(self.ladoA, self.ladoB, self.ladoC)

    def calcular_area(self) -> float:
        s = self.calcular_perimetro() / 2
        return math.sqrt(s * (s - self.ladoA) * (s - self.ladoB) * (s - self.ladoC))


a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
t = Triangulo(a, b, c)
print(f"Perímetro: {t.calcular_perimetro():.2f}")
print(f"Área: {t.calcular_area():.2f}")
print(f"Maior lado: {t.get_maior_lado():.2f}")
