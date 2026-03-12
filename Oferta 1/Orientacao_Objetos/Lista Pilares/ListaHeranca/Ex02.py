# 2 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir 
# os seguintes atributos:
#  Matricula; Nome; Idade;  
#  Subclasses:
#  Defina as subclasses de Pessoa serão Aluno e Professor, estas devem conter além dos atributos 
# herdados de Pessoa seus atributos identificadores, ex: Classe Aluno (NOTAS; MEDIA). 
#  Classe Professor (Formacao, Disciplina, Carga Horária e Salario)
#  Você deve criar métodos específicos para cada subclasse, ex: calcular_media, estudar, lecionar

class Pessoa:
    def __init__(self, matricula: str, nome: str, idade: int):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, matricula: str, nome: str, idade: int, notas: list[float]):
        super().__init__(matricula, nome, idade)
        self.notas = notas

    def calcular_media(self) -> float:
        return sum(self.notas) / len(self.notas)

    def estudar(self) -> None:
        print(f"{self.nome} está estudando.")


class Professor(Pessoa):
    def __init__(
        self,
        matricula: str,
        nome: str,
        idade: int,
        formacao: str,
        disciplina: str,
        carga_horaria: int,
        salario: float,
    ):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self) -> None:
        print(f"\nProfessor {self.nome} está lecionando {self.disciplina}.\n")



prof = Professor(
    "P001",
    "Mariano",
    35,
    formacao="Doutorado",
    disciplina="Matemática",
    carga_horaria=20,
    salario=4500.0,
)
prof.lecionar()

aluno = Aluno("A001", "Pedro", 20, [7.5, 8.0, 6.5])
aluno.estudar()
print(f"Média do aluno {aluno.nome}: {aluno.calcular_media():.2f}")

aluno2 = Aluno("A002", "Joaquim", 22, [9.0, 8.5, 9.5])
aluno2.estudar()
print(f"Média do aluno {aluno2.nome}: {aluno2.calcular_media():.2f}")