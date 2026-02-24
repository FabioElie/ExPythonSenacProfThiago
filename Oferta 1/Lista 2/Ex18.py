altura = float(input("Digite a sua altura: "))
sexo = str(input("Qual o seu sexo? F - Feminino, M - Masculino: ")).upper()

if (sexo =="M"):
    print(f"O seu peso ideal é de {(72.7 * altura) -58}kg")

if (sexo=="F"):
    print(f"O seu peso ideal é de {(62.1 * altura) -44.7}kg")
    