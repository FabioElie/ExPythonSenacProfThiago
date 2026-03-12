# 5 - Classe Funcionário: Um banco mantém contas de clientes armazenando o número 
# da conta, o nome do cliente e o saldo atual da conta. Crie uma classe que modele um 
# Conta-Corrente.
#  Nome; Sobrenome; Horas_trabalhadas; Valor_hora;
#  A classe deve ter o seguintes métodos:
#  O método nomeCompleto deve escrever na tela o atributo nome concatenado ao atributo 
# sobrenome.
#  O método calcularSalario faz o cálculo de quanto o funcionário irá receber no mês, 
# multiplicando o atributo horasTrabalhadas pelo atributo valorPorHora. Em seguida, 
# escreve o valor na tela.
#  O método incrementarHoras adiciona um valor passado por parâmetro ao valor já 
# existente no atributo valorPorHora

class Funcionario:
    def __init__(self, nome: str, sobrenome: str, horas_trabalhadas: float, valor_hora: float):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self) -> None:
        print(f"{self.nome} {self.sobrenome}")

    def calcular_salario(self) -> float:
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário: R$ {salario:.2f}")
        return salario

    def incrementar_horas(self, horas: float) -> None:
        if horas > 0:
            self.horas_trabalhadas += horas
        else:
            print("Horas a incrementar devem ser positivas.")


f = Funcionario("Ana", "Souza", 160, 25.0)
f.nome_completo()
f.calcular_salario()
f.incrementar_horas(10)
f.calcular_salario()
