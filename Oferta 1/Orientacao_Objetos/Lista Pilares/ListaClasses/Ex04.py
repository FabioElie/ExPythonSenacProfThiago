# 4 - Classe Conta: Um banco mantém contas de clientes armazenando o número da conta, o 
# nome do cliente e o saldo atual da conta. Crie uma classe que modele um Conta-Corrente.
#  Nome;
#  CPF;
#  Numero;
#  Saldo;
#  A classe deve ter o seguintes métodos:
#  Depositar()
#  Sacar()  -  OBS: somente enquanto a conta possuir saldo positivo
#  Imprimir saldo()


class Conta:
    def __init__(self, nome: str, cpf: str, numero: str, saldo: float = 0.0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
        if self.saldo - valor < 0:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        return True

    def imprimir_saldo(self) -> None:
        print(f"Saldo atual: R$ {self.saldo:.2f}")


c = Conta("Carlos", "123.456.789-00", "00012345-6", 100.0)
c.imprimir_saldo()
c.depositar(50)
c.imprimir_saldo()
sucesso = c.sacar(30)
print(f"Saque realizado. Saldo restante: R$ {c.saldo:.2f}" if sucesso else "Falha no saque. Saldo insuficiente.")
c.imprimir_saldo()
c.sacar(200)
c.imprimir_saldo()
