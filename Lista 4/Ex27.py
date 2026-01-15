A = int(input("Informe um numero: "))

fatorial = 1
sequencia = ""

for i in range(A, 0, -1):
    fatorial *= i
    sequencia += str(i)
    if i > 1:
        sequencia += " x "

print(f"{A}! = {sequencia} = {fatorial}")
