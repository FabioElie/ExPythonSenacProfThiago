lista = []

for num in range(0,10):
    numero = int(input("Digite um número: "))
    if numero > 0:
        lista.append(numero)

print(f"A média é {sum(lista) / len(lista)}")