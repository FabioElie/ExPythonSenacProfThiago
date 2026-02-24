soma = 0
qtd = 0
media = 0
soma_pares = 0
qtd_pares = 0
media_pares = 0

numero = float(input("Digite o primeiro numero: "))
menor = numero
maior = numero
soma += numero
qtd += 1

if numero % 2 == 0:
        soma_pares += numero
        qtd_pares += 1
        media_pares = soma_pares / qtd_pares

while numero != 0:
    numero = float(input("Digite um numero: "))
    if numero != 0:
        qtd += 1
        soma += numero

        if numero > maior:
            maior = numero

        if numero < menor and not numero == 0:
            menor = numero

        if numero % 2 == 0:
            soma_pares += numero
            qtd_pares += 1
            media_pares = soma_pares / qtd_pares

        media = soma / qtd


print(f"A SOMA dos numeros é {soma}.")
print(f"A QUANTIDADE de numeros digitados é {qtd}.")
print(f"A MÉDIA dos numeros digitados é {media}.")
print(f"O MAIOR numero é {maior}.")
print(f"O MENOR numero é {menor}.")
print(f"A MÉDIA dos numeros PARES digitados é {media_pares}.")
