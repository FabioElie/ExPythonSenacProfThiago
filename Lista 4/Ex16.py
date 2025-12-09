lista = []
numero = int(input("Digite um número: "))
if(numero % 2 != 0):
    for num in range(0,numero+1):
            if( num % 2 != 0):
                lista.append(num)
else:
      print("O numero nao é impar")

for num in lista:
        print(num)