# 3 - Classe Aluno: Crie uma classe que modele um aluno. Esta classe deve possuir os 
# seguintes atributos:
#  Nome;
#  RA;
#  Nota 1, nota 2, nota 3, nota 4;
#  A classe deve ter o seguintes método:
#  Mostrar_situacao: (APROVADO / EXAME / REPROVADO). Considere que, nesse caso, a média final 
# é calculada pela média aritmética simples de todas as notas e que o aluno é aprovado 
# somente se obtiver média maior ou igual a sete. Exame entre 5 e 6.9. Reprovado abaixo de 5
#  A situação será retornada a partir das notas obtidas pelo aluno

class Aluno:
    def __init__(self, nome: str, ra: str, nota1: float, nota2: float, nota3: float, nota4: float):
        self.nome = nome
        self.ra = ra
        self.notas = [nota1, nota2, nota3, nota4]

    def calcular_media(self) -> float:

        return sum(self.notas) / len(self.notas)

    def mostrar_situacao(self) -> str:
        media = self.calcular_media()
        if media >= 7.0:
            return "APROVADO"
        elif media >= 5.0:
            return "EXAME"
        else:
            return "REPROVADO"



aluno = Aluno("Maria", "12345", 8.0, 6.0, 7.5, 9.0)
print(f"Aluno: {aluno.nome} (RA: {aluno.ra})")
print(f"Média: {aluno.calcular_media():.2f}")
print(f"Situação: {aluno.mostrar_situacao()}")
