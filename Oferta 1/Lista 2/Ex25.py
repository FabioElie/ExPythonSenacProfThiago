opcao = int(input("CALCULADORA: Qual operação deseja fazer? 1-Somar 2-Subtrair 3-Multiplicar 4-Dividir "))

match opcao:
    case 1:
        n1 = input("Qual o primeiro número? ")
        n2 = input("Qual o segundo número? ")
        print(f"O resultado é {n1+n2}")
    
    case 2:
        n1 = input("Qual o primeiro número? ")
        n2 = input("Qual o segundo número? ")
        print(f"O resultado é {n1-n2}")
   
    case 3:
        n1 = input("Qual o primeiro número? ")
        n2 = input("Qual o segundo número? ")
        print(f"O resultado é {n1*n2}")
    
    case 4:
        n1 = input("Qual o primeiro número? ")
        n2 = input("Qual o segundo número? ")
        print(f"O resultado é {n1/n2}")
    
    case _:
        print("Opção Invalida")