soma = 0
listaDeNumeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º numero: "))
    soma = soma + numero
    listaDeNumeros.append(numero)

print(f'A soma dos numeros é: {soma}')
print(listaDeNumeros)
print(listaDeNumeros.count(5))