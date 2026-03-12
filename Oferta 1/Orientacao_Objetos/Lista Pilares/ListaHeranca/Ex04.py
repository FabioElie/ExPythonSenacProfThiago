# 4 - Classe Passagem: Crie uma super classe que modele uma Passagem. Esta classe deve 
# possuir os seguintes atributos:
#  Preco;
#  Assento;
#  Método:
#  alterar_preco() e escolher_assento();
#  Subclasses:
#  Defina a subclasse PassagemBus e PassagemAviao com os seguintes atributos: portaodeembarque 
# e checkin para classe PassagemAviao, placa e leito par PassagemBus;
#  Crie um novo método específico para cada subclasse. Ex: decolar() e abastecer()


class Passagem:
    def __init__(self, preco: float, assento: str):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_valor: float) -> None:
        if novo_valor >= 0:
            self.preco = novo_valor
        else:
            print("Preço não pode ser negativo.")

    def escolher_assento(self, novo_assento: str) -> None:
        self.assento = novo_assento
        print(f"Assento escolhido: {self.assento}")


class PassagemAviao(Passagem):
    def __init__(
        self,
        preco: float,
        assento: str,
        portao_embarque: str,
        checkin: bool,
    ):
        super().__init__(preco, assento)
        self.portao_embarque = portao_embarque
        self.checkin = checkin

    def decolar(self) -> None:
        if self.checkin:
            print(f"Avião decolando pelo portão {self.portao_embarque}.")
        else:
            print("Não pode decolar antes do check-in.")


class PassagemBus(Passagem):
    def __init__(
        self,
        preco: float,
        assento: str,
        placa: str,
        leito: bool,
    ):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self) -> None:
        print(f"Ônibus placa {self.placa} está abastecendo.")


aviao = PassagemAviao(500.0, "12A", "B3", True)
aviao.escolher_assento("14C")
aviao.decolar()
aviao.alterar_preco(550.0)
print(f"Preço atual: R$ {aviao.preco:.2f}\n")

bus = PassagemBus(120.0, "3B", "XYZ-1234", leito=True)
bus.abastecer()
bus.escolher_assento("4C")
print(f"Preço do ônibus: R$ {bus.preco:.2f}")
