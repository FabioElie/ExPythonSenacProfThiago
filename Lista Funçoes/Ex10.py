def financiamento(valorVeiculo, valorEntrada, taxaJuros, qtdParcelas):
    
    valorFinanciado = valorVeiculo - valorEntrada
    montanteFinal = valorFinanciado * (1 + taxaJuros) ** qtdParcelas
    jurosTotais = montanteFinal - valorFinanciado
    valorParcela = montanteFinal / qtdParcelas

    print(f"Valor do veículo: R$ {valorVeiculo:.2f}")
    print(f"Valor da entrada: R$ {valorEntrada:.2f}")
    print(f"Valor financiado: R$ {valorFinanciado:.2f}")
    print(f"Taxa de juros: {taxaJuros*100:.2f}% ao mês")
    print(f"Quantidade de parcelas: {qtdParcelas}")
    print(f"Valor aproximado de cada parcela: R$ {valorParcela:.2f}")
    print(f"Total pago ao final: R$ {montanteFinal:.2f}")
    print(f"Total de juros pagos: R$ {jurosTotais:.2f}")


financiamento(50000, 10000, 0.02, 60)
