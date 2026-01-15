# Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais 
# de 0 até N em ordem decrescente. 
lista = []
numero = int(input("Digite um número: "))
for num in range(0,numero+1):
        lista.append(num)

lista.reverse()
for num in lista:
    print(num)