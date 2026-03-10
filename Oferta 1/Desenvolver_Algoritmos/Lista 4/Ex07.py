# Escreva um programa que leia 10 inteiros e imprima sua média. 
lista = []

for num in range(0,10):
    lista.append(int(input("Digite um número: ")))

print(f"A média é {sum(lista) / len(lista)}")