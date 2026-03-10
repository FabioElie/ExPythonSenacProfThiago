#  Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50 
# primeiros números pares. 
soma = 0
qtdPares = 0

for numero in range(0,101):
    if(numero % 2 == 0 and qtdPares <= 50):
        soma += numero
        qtdPares += 1

    if qtdPares == 50:
            break

print("A soma dos 50 primeiros números pares é:", soma)
