#  Crie um programa que apresente um menu de opções para o cálculo das seguintes operações 
# entre dois números. 
# • adição (opção 1) 
# • subtração (opção 2) 
# • multiplicação (opção 3) 
# • divisão (opção 4). 
# • saída (opção 5) 
# O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do 
# resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção 
# de saída (opção 5).

opcao = ""

while opcao != "5":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("\n--- Menu de Operações ---")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Saída")
    
    opcao = input("Escolha a operação desejada: ")

    if opcao == "5":
        print("Encerrando o programa...")
        break
    

    if opcao == "1":
        resultado = num1 + num2
        print("Soma é:", num1, "+", num2, "=", resultado)
        
    elif opcao == "2":
        resultado = num1 - num2
        print("Subtração é:", num1, "-", num2, "=", resultado)
        
    elif opcao == "3":
        resultado = num1 * num2
        print("Multiplicação é:", num1, "*", num2, "=", resultado)
        
    elif opcao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print("Divisão é:", num1, "/", num2, "=", resultado)
        else:
            print("Erro: Divisão por zero não é permitida.")
    
    else:
        print("Opção inválida! Tente novamente.")

print("Programa finalizado.")