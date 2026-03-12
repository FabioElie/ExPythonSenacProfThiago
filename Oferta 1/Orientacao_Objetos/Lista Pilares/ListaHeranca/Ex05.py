# 5 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir 
# os seguintes atributos:
#  Nome; Telefone; E-mail; Endereço;
#  Métodos:
#  negociar: deve printar uma mensagem de negociação;
#  Subclasses:
#  Defina as subclasses de Pessoa serão Física e Jurídica, estas devem conter além dos atributos 
# herdados de Pessoa seus atributos identificadores, ex: CPF, CNPJ.
#  Além de herdar o método negociar() crie métodos específicos para as subclasses

class Pessoa:
    def __init__(self, nome: str, telefone: str, email: str, endereco: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self) -> None:
        print(f"{self.nome} está negociando.")


class PessoaFisica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def apresentar_documento(self) -> None:
        print(f"CPF: {self.cpf}")


class PessoaJuridica(Pessoa):
    def __init__(
        self,
        nome: str,
        telefone: str,
        email: str,
        endereco: str,
        cnpj: str,
    ):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def apresentar_certidao(self) -> None:
        print(f"CNPJ: {self.cnpj}")


pf = PessoaFisica(
    "Carlos Silva",
    "(11) 99999-0000",
    "carlos@example.com",
    "Rua A, 123",
    cpf="123.456.789-00",
)
pf.negociar()
pf.apresentar_documento()

pj = PessoaJuridica(
    "Empresa XYZ",
    "(11) 88888-0000",
    "contato@xyz.com",
    "Av. B, 456",
    cnpj="12.345.678/0001-90",
)
pj.negociar()
pj.apresentar_certidao()
