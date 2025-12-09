valor = float(input("Qual o valor do produto? "))

if (valor<=50):
    print(f"O Valor do produto era R${valor:.2f} e será vendido por R${valor * 1.45:.2f}")
else:
    print(f"O Valor do produto era R${valor:.2f} e será vendido por R${valor * 1.30:.2f}")