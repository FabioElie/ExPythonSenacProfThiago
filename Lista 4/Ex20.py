# Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser 
# informado o número de dados lidos e número de valores pares. O processo termina quando for 
# digitado o número 0. 
quantidade: int = 0
pares: int = 0

while True:
    numero = int(input("Digite um número inteiro (0 para encerrar): "))

    if numero == 0:
        break


    quantidade += 1

    if numero % 2 == 0:
        pares += 1

print(f"Quantidade de números lidos: {quantidade}")
print(f"Quantidade de números pares: {pares}")