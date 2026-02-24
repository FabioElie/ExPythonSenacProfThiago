# Crie uma função que retorne uma lista com valor 
# padrão. Para esta função, consideraremos como argumentos 
# de entrada a quantidade de elementos e o valor padrão a 
# ser atribuído a todos eles. Exemplo de retorno:
# [1,1,1,1,1,1,1,1]
# [“A”,”A”,”A”,”A”

def criar_lista(quantidade, valor_padrao):
    lista = []
    for elemento in range(quantidade):
        lista.append(valor_padrao)
    return lista

print(criar_lista(8, 1))
print(criar_lista(4, "A"))