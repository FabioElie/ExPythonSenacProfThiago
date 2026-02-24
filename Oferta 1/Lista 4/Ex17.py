# Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros 
# números naturais.
lista = []
numero = int(input("Digite um número: "))
for num in range(0,numero+1):
        lista.append(num)

print(sum(lista))