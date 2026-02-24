dia = int(input("Digite o numero do dia da semana: 1-Domingo 2-Segunda 3-Terça 4-Quarta 5-Quinta 6-Sexta 7-Sabado "))

match dia:
    case 1:
        print("Hoje é Domingo")
    case 2:
        print("Hoje é Segunda")
    case 3:
        print("Hoje é Terça")
    case 4:
        print("Hoje é Quarta")
    case 5:
        print("Hoje é Quinta")
    case 6:
        print("Hoje é Sexta")
    case 7:
        print("Hoje é Sábado")
    case _:
        print("Numero Invalido")
    