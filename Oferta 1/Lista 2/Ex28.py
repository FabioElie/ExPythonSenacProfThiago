opcao = int(input("""CALCULADORA: 
                  Qual operação deseja fazer? 
                  1-Somar 
                  2-Diferença 
                  3-Multiplicar
                  4-Dividir """))

n1 = float(input("Qual o primeiro número? "))
n2 = float(input("Qual o segundo número? "))

match opcao:
    case 1:
        print(f"O resultado é {n1+n2}")

    case 2:
        if(n1>n2):
            print(f"A diferença é {n1-n2}")
        elif(n2>n1):
            print(f"A diferença é {n2-n1}")
        else:
            print(f"Os numeros sao iguais e não possuem diferenca")
    
    case 3:
        print(f"O resultado é {n1*n2}")
    
    case 4:
        if(n2==0):
            print("O denominador não pode ser 0")
        else:
            print(f"O resultado é {n1/n2}")
    
    case _:
        print("Opção Invalida")