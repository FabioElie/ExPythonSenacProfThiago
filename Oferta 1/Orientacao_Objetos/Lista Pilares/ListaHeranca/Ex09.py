# 9 - Classe Compra: Crie uma super classe que modele uma Venda. Esta classe deve possuir 
# os seguintes atributos:
#  Numero; Produto; Valor; Valor_total = 0;
#  Método:
#  calcular_valor_total(): deve somar ao valor_total o imposto de 17% do ICMS + o Frete de 
# 5% sobre o valor do protudo;
#  Subclasses:
#  Defina as subclasses Avista e Parcelada, na classe de compra a vista deve ter o atributo desconto e na classe 
# Parcelada numero de parcelas.
#  Em cada subclasse definir um método que retorna o preço com desconto ou o valor das parcelas.


class Venda:
    def __init__(self, numero: str, produto: str, valor: float):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0.0

    def calcular_valor_total(self) -> float:
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        return self.valor_total


class Avista(Venda):
    def __init__(self, numero: str, produto: str, valor: float, desconto: float):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def preco_com_desconto(self) -> float:
        total = self.calcular_valor_total()
        return total - self.desconto


class Parcelada(Venda):
    def __init__(self, numero: str, produto: str, valor: float, parcelas: int):
        super().__init__(numero, produto, valor)
        self.parcelas = parcelas

    def valor_parcela(self) -> float:
        total = self.calcular_valor_total()
        return total / self.parcelas


produto = Avista("001", "Notebook", 2000.0, desconto=100.0)
print("Valor Original do Produto:", produto.valor)
print("Valor do Desconto:", produto.desconto)
print("Valor do frete e ICMS:", produto.calcular_valor_total() - produto.valor)
print("Total à vista com desconto:", produto.preco_com_desconto())

produto = Parcelada("002", "Geladeira", 3000.0, parcelas=10)
print("\nValor Original do Produto:", produto.valor)
print("Valor do frete e ICMS:", produto.calcular_valor_total() - produto.valor)
print("Valor de cada parcela:", produto.valor_parcela())
