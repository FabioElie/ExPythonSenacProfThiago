import math

def calcularTempo (minutos):
    if minutos <= 15:
        print(f"Saida Liberada, tempo cortesia de até 15 minutos.")
        return 0
    if minutos > 15 and minutos <= 60:
        valorTotal = 9
        return valorTotal
    if minutos > 60:
        qtdHorasArredondadas = math.ceil(minutos / 60)
        valorMinimo = 9
        valorHoraAdicional = 1.50
        qtdHorasAdicionais = qtdHorasArredondadas - 1
        valorTotal= (qtdHorasAdicionais * valorHoraAdicional) + valorMinimo 
        return valorTotal
       
custo = calcularTempo(130)

print(f"Voce deve pagar R${custo:.2f} para ser liberado.")