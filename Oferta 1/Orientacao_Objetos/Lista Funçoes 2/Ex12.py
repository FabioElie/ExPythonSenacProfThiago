# Crie uma função que receba uma lista 
# como argumento, os valores da lista devem ser 
# numéricos, por fim retorne a média desses 
# valores

valores = [10, 20, 30, 40]

def calcular_media(lista):
    soma = 0
    for numero in lista:
        soma += numero
    
    media = soma / len(lista)
    return media

resultado = calcular_media(valores)
print(resultado)