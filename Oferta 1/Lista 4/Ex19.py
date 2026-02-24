# Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um 
# dos algarismos que compõem o número. 
soma = 0
numero = (input("Digite um numero entre 100 e 9999: "))

if(numero<100 or numero>9999):
    print("Numero Invalido")
else:
    numero = str(numero)
    for num in numero:
        soma += int(num)

print("A soma dos algarismos é:", soma)
