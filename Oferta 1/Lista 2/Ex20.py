prova1 = int(input("Digite a nota da primeira prova: "))
prova2 = int(input("Digite a nota da segunda prova: "))
prova3 = int(input("Digite a nota da terceira prova: "))

media = (prova1 + prova2 + (prova3 * 2))/3

print(f"O aluno foi aprovado com a média de {media:.2f}" if media>=60 else f"Aluno Reprovado com a média de {media:.2f}")