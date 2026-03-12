# 1 - Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os 
# seguintes atributos:
#  Nome
#  Idade
#  Endereço
#  A classe deve ter os seguintes métodos:
#  Mostrar nome;
#  Alterar a idade;
#  Imprimir endereço

class Pessoa:
    def __init__(self, nome: str, idade: int, endereco: str):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_nome(self) -> None:
        print(f"Nome: {self.nome}")

    def alterar_idade(self, nova_idade: int) -> None:
        self.idade = nova_idade

    def imprimir_endereco(self) -> None:
        print(f"Endereço: {self.endereco}")


pessoa1 = Pessoa("João", 30, "Rua A")
pessoa1.mostrar_nome()
pessoa1.imprimir_endereco()
pessoa1.alterar_idade(31)
print(f"Idade atualizada: {pessoa1.idade}")
