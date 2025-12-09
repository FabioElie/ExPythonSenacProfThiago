lista = []
quantidade = int(input("Quantos números seram digitados? "))
numero = int(input("Digite o 1º número: "))
lista.append(numero)
maior = numero

for num in range(1,quantidade):
    numero = int(input("Digite o próximo número: "))
    lista.append(numero)
    if numero > maior:
        maior = numero

print(f"O maior numero é {maior}")