# 6 - Classe Funcionário: Crie uma super classe que modele um Funcionário genérico. Esta 
# classe deve possuir os seguintes atributos:
#  Nome;
#  Matricula;
#  Salario;
#  Método:
#  Bater_ponto(): deve criar uma lista de pontos do funcionário, pode ser booleana 0 ou 1;
#  Subclasses:
#  Defina as subclasses de Funcionário, exemplo Vendedor e Gerente. Após a criação das subclasses 
# você deve criar atributos e métodos específicos de cada subclasse;
#  Ex: atributo comissão e método bater_meta() para Vendedor e atributo senha para o Gerente.


class Funcionario:
    def __init__(self, nome: str, matricula: str, salario: float):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self, presente: bool) -> None:
        self.pontos.append(1 if presente else 0)
        print(f"Registro de Ponto: {f'{self.nome} estava Presente' if presente else f'{self.nome} estava Ausente'}")


class Vendedor(Funcionario):
    def __init__(self, nome: str, matricula: str, salario: float, comissao: float):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
        self.vendas = 0.0

    def bater_meta(self, valor_venda: float) -> None:
        self.vendas += valor_venda
        if self.vendas >= self.comissao:
            print(f"{self.nome} bateu a meta com {self.vendas:.2f}!" )
        else:
            print(f"{self.nome} ainda não bateu a meta: {self.vendas:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome: str, matricula: str, salario: float, senha: str):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def acessar_sistema(self, senha: str) -> None:
        if senha == self.senha:
            print(f"Acesso concedido ao gerente. {self.nome} está acessando o sistema.")
        else:
            print("Senha incorreta.")


vend = Vendedor("Ana", "V001", 2000.0, comissao=5000.00)
vend.bater_ponto(False)
vend.bater_meta(3000)


ger = Gerente("Andre", "G001", 5000.00, senha="1234")
ger.bater_ponto(True)
ger.acessar_sistema("1234")
