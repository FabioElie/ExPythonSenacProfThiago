# Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3 
# x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente 
# (y) e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para 
# resolver o problema utilize estrutura de repetição.
base = float(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

resultado = 1

for i in range(expoente):
    resultado *= base

print(f"O resultado de {base}^{expoente} é {resultado}")