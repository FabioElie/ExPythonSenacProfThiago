lista = []
numero = int(input("Digite um número: "))
for num in range(0,numero+1):
        if( num % 2 == 0):
            lista.append(num)

for num in lista:
        print(num)