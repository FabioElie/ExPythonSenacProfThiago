def tabela (valor):
    qtd = 1
    while qtd <= 50:
        valorTotal = valor * qtd
        print(f"{qtd} - R$ {valorTotal:.2f}")
        qtd += 1
    

tabela(1.99)