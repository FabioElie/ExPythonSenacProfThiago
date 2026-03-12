#  Classe Agenda: crie uma classe que represente uma agenda de tarefas. Esta classe 
# deve possuir os seguintes atributos:
#  Dia;
#  Mês;
#  Ano;
#  Anotação;
#  A classe deve ter os seguintes métodos:
#  validar_data();
#  anotar_tarefa();
#  Mostrar_anotação();


import datetime

class Agenda:
    def __init__(self, dia: int, mes: int, ano: int, anotacao: str = ""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self) -> bool:
        try:
            datetime.date(self.ano, self.mes, self.dia)
            return True
        except ValueError:
            return False

    def anotar_tarefa(self, texto: str) -> None:
        self.anotacao = texto

    def mostrar_anotacao(self) -> None:
        if self.anotacao:
            print(f"Anotação para {self.dia:02d}/{self.mes:02d}/{self.ano}: {self.anotacao}")
        else:
            print("Nenhuma anotação para esta data.")


agenda = Agenda(29, 2, 2024)
print("Data válida?", "Sim" if agenda.validar_data() else "Não")
agenda.anotar_tarefa("Reunião às 14h")
agenda.mostrar_anotacao()
agenda2 = Agenda(31, 11, 2023)
print("Data válida?", "Sim" if agenda2.validar_data() else "Não")
agenda2.mostrar_anotacao()

