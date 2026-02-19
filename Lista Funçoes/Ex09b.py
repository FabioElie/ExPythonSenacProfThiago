import math
porc_pis = 0.033
porc_cofins = 0.02
porc_icms = 0.17
def calcularTempo (minutos):
    if minutos <= 15:
        print(f"Saida Liberada, tempo cortesia de até 15 minutos.")
        return 0
    if minutos > 15 and minutos <= 60:
        valorTotal = 9
        print("Tempo 1.0 horas")
        return valorTotal
    if minutos > 60:
        qtdHorasArredondadas = math.ceil(minutos / 60)
        valorMinimo = 9
        valorHoraAdicional = 1.50
        qtdHorasAdicionais = qtdHorasArredondadas - 1
        valorTotal= (qtdHorasAdicionais * valorHoraAdicional) + valorMinimo
        print(f"Tempo {qtdHorasArredondadas:.1f} horas")
        return valorTotal
       
custo = calcularTempo(240)

valor_pis = custo * porc_pis
valor_cofins = custo * porc_cofins
valor_icms = custo * porc_icms
imposto_total = (valor_pis+valor_cofins+valor_icms)
print(f"PIS R$ {valor_pis:.2f}")
print(f"COFINS R$ {valor_cofins:.2f}")
print(f"ICMS R$ {valor_icms:.2f}")
print(f"IMPOSTOS R$ {imposto_total:.2f}")
print(f"Total R$ {custo:.2f}")