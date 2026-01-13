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