from datetime import date


class NotaFiscal:
    def __init__(
        self,
        numero: str,
        tipo: str,
        serie: int,
        cnpj: str,
        razao_social: str,
        data: date,
        valor_produtos: float,
        icms: float,
        frete: float,
        ipi: float,
    ):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0.0

    def obter_numero(self) -> str:
        return self.numero

    def obter_data_emissao(self) -> date:
        return self.data

    def alterar_razao_social(self, nova_razao: str) -> None:
        self.razao_social = nova_razao

    def calcular_valor_total(self) -> float:
        total = self.valor_produtos + self.frete + self.icms + self.ipi
        self.valor_total = total
        return total


nf = NotaFiscal(
    numero="12345",
    tipo="Saída",
    serie=1,
    cnpj="12.345.678/0001-90",
    razao_social="Empresa X Ltda",
    data=date(2024, 3, 12),
    valor_produtos=1000.0,
    icms=180.0,
    frete=50.0,
    ipi=20.0,
)

print("Número:", nf.obter_numero())
print("Data emissão:", nf.obter_data_emissao())
print("Valor total calculado:", nf.calcular_valor_total())
nf.alterar_razao_social("Empresa Y SA")
print("Nova razão social:", nf.razao_social)
