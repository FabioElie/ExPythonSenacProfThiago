# Crie um programa que receba dois números. Calcule e mostre: 
# • a soma dos números pares desse intervalo de números, incluindo os números digitados; 
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados; 
soma: int = 0
multiplicacao: int = 1

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

inicio = min(num1, num2)
fim = max(num1, num2)

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma += i
    else:
        multiplicacao *= i

print(f"Soma dos números pares no intervalo: {soma}")
print(f"Multiplicação dos números ímpares no intervalo: {multiplicacao}")