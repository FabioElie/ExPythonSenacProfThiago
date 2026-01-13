soma = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f"Soma dos múltiplos de 3 ou 5 abaixo de 1000: {soma}")
