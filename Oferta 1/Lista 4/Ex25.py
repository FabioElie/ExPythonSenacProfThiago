# Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando 
# for informada a idade 0), e calcule a idade média desse grupo. 
idades = []

while True:
    idade = int(input("Digite a idade da pessoa, caso deseje encerrar o programa digite 0: "))
    
    if idade == 0:
        print("Encerrando Programa!")
        break

    idades.append(idade)

if len(idades) > 0:
    media = sum(idades) / len(idades)
    print("Idades Informadas", idades)
    print(f"Idade média do grupo: {media:.2f}")
else:
    print("Nenhuma idade válida foi informada.")