# 9 - Classe Aluno_Academia: Uma academia mantem registro de seus alunos e precisa 
# armazenar os seguintes atributos:
#  Nome, Idade, Peso, Altura, Mensalidade (valor default: R$ 120,00)
#  A academia faz um desconto especial para menores de idade, portanto, é 
# necessário saber distinguir entre um aluno maior e menor. Além disso, a 
# academia também tem interesse em acompanhar o desempenho de seus alunos, 
# por isso, ela também necessita conhecer o índice de massa corporal (IMC) deles, 
# para isso a classe deve ter os seguintes métodos:
#  Calcular_IMC()
#  Obter_valor_mensalidade(

class AlunoAcademia:
    def __init__(self, nome: str, idade: int, peso: float, altura: float, mensalidade: float = 120.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_imc(self) -> float:
        if self.altura <= 0:
            raise ValueError("Altura deve ser maior que zero para calculo de IMC")
        return self.peso / (self.altura ** 2)

    def is_menor_idade(self) -> bool:
        """Verifica se o aluno é menor de idade (< 18 anos)."""
        return self.idade < 18

    def obter_valor_mensalidade(self) -> float:
        if self.is_menor_idade():
            return self.mensalidade * 0.5
        return self.mensalidade


aluno1 = AlunoAcademia("Rafael", 17, 70.0, 1.75)
print(f"IMC de {aluno1.nome}: {aluno1.calcular_imc():.2f}")
print(f"Mensalidade: R$ {aluno1.obter_valor_mensalidade():.2f}")

aluno2 = AlunoAcademia("Larissa", 21, 90.0, 1.65)
print(f"IMC de {aluno2.nome}: {aluno2.calcular_imc():.2f}")
print(f"Mensalidade: R$ {aluno2.obter_valor_mensalidade():.2f}")
