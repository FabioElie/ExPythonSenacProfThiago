# Crie uma função que receba como argumento uma lista, com 
# valores de qualquer tipo. A função deve imprimir todos os 
# elementos da lista numerando-os. Exemplo:
# 1, Pera
# 2, Uva
# 3, Maça
# 4, Salada mista

itens = ["Pera", "Uva", "Maça", "Salada mista"]

def listar_numerado(lista):
    i = 1
    for elemento in lista:
        print(f"{i} - {elemento}")
        i += 1

listar_numerado(itens)