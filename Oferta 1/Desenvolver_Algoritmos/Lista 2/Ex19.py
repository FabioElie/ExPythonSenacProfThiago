numero_digitado = input("Digite um número MAIOR que 0: ")

if int(numero_digitado) > 0:
    soma = 0
    for numero in numero_digitado:  
        soma += int(numero)         
    print(f"A soma dos numeros é {soma}")
else:
    print("Número é menor que 0!!!")
