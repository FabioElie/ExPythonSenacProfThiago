def somaImposto (taxaImposto, custo):
    valor = custo - (custo * (taxaImposto/100))
    return valor

novoValor = somaImposto(10, 200)
print(f"O valor apos o desconto do imposto é {novoValor} reais")