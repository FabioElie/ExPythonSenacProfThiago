numero = int(input("Digite um número inteiro: "))

soma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

print(f"Soma dos divisores de {numero}: {soma_divisores}")
