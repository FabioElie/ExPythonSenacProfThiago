lista = []
numero = int(input("Digite um número: "))
for num in range(0,numero+1):
        lista.append(num)

lista.reverse()
for num in lista:
    print(num)