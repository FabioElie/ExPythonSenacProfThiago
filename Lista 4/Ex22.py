soma: float = 0
quantidade: int = 0

while True:
    nota = float(input("Digite uma nota de 0 a 10: "))

    if nota < 0 or nota > 10:
        print("Nota fornecidad invalida")
        break
    soma += nota
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhuma nota válida foi informada.")