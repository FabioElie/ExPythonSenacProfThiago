# 3 - Classe Ingresso: Crie uma super classe que modele um Ingresso. Esta classe deve 
# possuir os seguintes atributos:
#  Preco;
#  Setor;
#  Método:
#  alterar_preco() e mostrar_setor();
#  Subclasses:
#  Defina a subclasse ingressoVIP com os seguintes atributos: camarote, open_bar, open_food, 
# estacionamento -> todos booleanos, True ou False;
#  Acrescente os métodos pegar_bebida() e acessar_camarote()

class Ingresso:
    def __init__(self, preco: float, setor: str):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco: float) -> None:
        if novo_preco >= 0:
            self.preco = novo_preco
        else:
            print("Preço não pode ser negativo.")

    def mostrar_setor(self) -> None:
        print(f"Setor: {self.setor}")


class IngressoVIP(Ingresso):
    def __init__(
        self,
        preco: float,
        setor: str,
        camarote: bool,
        open_bar: bool,
        open_food: bool,
        estacionamento: bool,
    ):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self) -> None:
        if self.open_bar:
            print("Bebida liberada no open bar!")
        else:
            print("Sem open bar nesta entrada.")

    def acessar_camarote(self) -> None:
        if self.camarote:
            print("Acesso ao camarote autorizado.")
        else:
            print("Este ingresso não permite acesso ao camarote.")



ingresso = Ingresso(100.0, "Arquibancada")
ingresso.mostrar_setor()
ingresso.alterar_preco(120.0)
print(f"Novo preço: R$ {ingresso.preco:.2f}\n")

vip = IngressoVIP(300.0, "Camarote", True, True, False, True)
vip.mostrar_setor()
vip.pegar_bebida()
vip.acessar_camarote()