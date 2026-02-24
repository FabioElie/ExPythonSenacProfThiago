numeros = []

qtdlinhas = int(input("Digite quantas linhas deseja: "))
qtdcolunas = int(input("Digite quantas colunas deseja: "))

for i in range(qtdlinhas):       
    linhas = []          
    for j in range(qtdcolunas):  
        numero = int(input(f"Digite um numero para a posicao [{i},{j}]: "))
        linhas.append(numero)
    numeros.append(linhas)

print("Matriz resultante:")
for linha in numeros:
    print(linha)
