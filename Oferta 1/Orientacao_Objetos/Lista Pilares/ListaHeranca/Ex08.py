# 8 - Classe Imóvel: Uma Imobiliária precisa de um sistema que controle o aluguel de seus 
# Imóveis. Para isto você deve definir em um módulo a super classe Imóvel com os seguintes 
# atributos:
#  InscricaoMunicipal; Valor_aluguel; IPTU;
#  Método:
#  obter_parcela_IPTU();
#  Set_valor_aluguel();
#  Subclasses:
#  Defina as subclasses de Imóvel sendo: Casa, Condomínio; Apartamento; Terreno e Chácara;
#  Defina os atributos específicos para cada sub classe, exemplo: piscina, sala_de_estar, 
#  Quartos, churrasqueira, área m², elevador, área_de_lazer,   .


class Imovel:
    def __init__(
        self,
        inscricao_municipal: str,
        valor_aluguel: float,
        iptu: float,
    ):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_iptu(self) -> float:
        return self.iptu / 12

    def set_valor_aluguel(self, novo_valor: float) -> None:
        if novo_valor >= 0:
            self.valor_aluguel = novo_valor
        else:
            print("Valor de aluguel não pode ser negativo.")


class Casa(Imovel):
    def __init__(
        self,
        inscricao_municipal: str,
        valor_aluguel: float,
        iptu: float,
        quartos: int,
        sala_estar: bool,
        piscina: bool,
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.sala_estar = sala_estar
        self.piscina = piscina


class Condominio(Imovel):
    def __init__(
        self,
        inscricao_municipal: str,
        valor_aluguel: float,
        iptu: float,
        area_lazer: bool,
        elevador: bool,
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_lazer = area_lazer
        self.elevador = elevador


class Apartamento(Imovel):
    def __init__(
        self,
        inscricao_municipal: str,
        valor_aluguel: float,
        iptu: float,
        quartos: int,
        area_m2: float,
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.area_m2 = area_m2


class Terreno(Imovel):
    def __init__(
        self,
        inscricao_municipal: str,
        valor_aluguel: float,
        iptu: float,
        area_m2: float,
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_m2 = area_m2


class Chacara(Imovel):
    def __init__(
        self,
        inscricao_municipal: str,
        valor_aluguel: float,
        iptu: float,
        area_m2: float,
        churrasqueira: bool,
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_m2 = area_m2
        self.churrasqueira = churrasqueira


casa = Casa("12345", 1500.0, 300.0, quartos=3, sala_estar=True, piscina=False)
print("IPTU parcelado:", casa.obter_parcela_iptu())
casa.set_valor_aluguel(1600.0)
print("Novo aluguel:", casa.valor_aluguel)

ap = Apartamento("23456", 1200.0, 250.0, quartos=2, area_m2=75.0)
print("Apartamento área:", ap.area_m2)

chacara = Chacara("34567", 2000.0, 400.0, area_m2=500.0, churrasqueira=True)
print("Chácara tem churrasqueira?", chacara.churrasqueira)
chacara.set_valor_aluguel(2200.0)
print("Novo aluguel da chácara:", chacara.valor_aluguel)

terreno = Terreno("45678", 800.0, 150.0, area_m2=1000.0)
print("Terreno área:", terreno.area_m2)
print("IPTU mensal do terreno:", terreno.obter_parcela_iptu())
print("Ótimo para um shopping center ou para construção de uma casa.")