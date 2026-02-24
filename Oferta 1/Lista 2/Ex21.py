trabalho_laboratorio = int(input("Digite a nota do trabalho de laboratório de 0 a 10: "))
avaliacao_semestral = int(input("Digite a nota da avaliação semestral de 0 a 10: "))
exame_final = int(input("Digite a nota do exame final de 0 a 10: "))

if (trabalho_laboratorio < 0 or trabalho_laboratorio > 10 or avaliacao_semestral < 0 or avaliacao_semestral > 10 or exame_final < 0 or exame_final > 10):
    print("Nota inválida")
else:
    media = (trabalho_laboratorio*2 + avaliacao_semestral*3 + exame_final*5)/10

    if (0>media<=2.9):
        print(f"O aluno foi reprovado com a média de {media:.2f}")
    elif(3>=media<=5.9):
        print(f"O aluno está de recuperação com a média de {media:.2f}")
    else:
        print(f"O aluno foi aprovado com a média de {media:.2f}")
