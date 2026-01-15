# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
lista = []

numero = int(input("Digite o 1º número: "))
lista.append(numero)
maior = numero
menor = numero

for num in range(0,10):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f"O maior numero é {maior}")
print(f"O menor numero é {menor}")