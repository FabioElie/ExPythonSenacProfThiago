# Crie um programa que leia um número inteiro N e depois imprima os N primeiros números 
# naturais ímpares.
numero = int(input("Digite um numero "))

while numero > 0:
    if(numero % 2 != 0):
        print(numero)
    numero -= 1
