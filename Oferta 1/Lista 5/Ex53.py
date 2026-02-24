#  Crie um programa para a Academia BemMaisFort. Neste programa você deve receber os dados 
# de 25 pessoas. Sendo: Idade, Sexo, Altura, Peso. No final o programa deve calcular e imprimir:  
# a) a idade da pessoa mais velha  
# b) a idade da pessoa mais nova 
# c) a altura do mais alto 
# d) altura do mais baixo 
# e) o maior peso 
# f) 
# a média de Altura e a Média de IMC;  
# g) porcentagem de Sexo Masculino  
# h) porcentagem de Sexo Feminino

total_pessoas = 25
idades = []
alturas = []
pesos = []
imcs = []
qtd_masculino = 0
qtd_feminino = 0

for i in range(total_pessoas):
    print(f"\nPessoa {i + 1}")

    idade = int(input("Digite a idade: "))
    sexo = input("Qual o sexo (M/F)? ").upper()
    altura = float(input("Qual a altura em metros (ex: 1.83): "))
    peso = float(input("Qual o peso em kg (ex: 68.3): "))

    imc = peso / (altura ** 2)

    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    imcs.append(imc)

    if sexo == 'M':
        qtd_masculino += 1
    elif sexo == 'F':
        qtd_feminino += 1

mais_velho = max(idades)
mais_novo = min(idades)

mais_alto = max(alturas)
mais_baixo = min(alturas)

mais_pesado = max(pesos)

media_altura = sum(alturas) / total_pessoas
media_imc = sum(imcs) / total_pessoas

porcentual_masculino = (qtd_masculino / total_pessoas) * 100
porcentual_feminino = (qtd_feminino / total_pessoas) * 100

print(f"Idade da pessoa mais velha: {mais_velho} anos")
print(f"Idade da pessoa mais nova: {mais_novo} anos")
print(f"Altura da pessoa mais alta: {mais_alto:.2f} m")
print(f"Altura da pessoa mais baixa: {mais_baixo:.2f} m")
print(f"Maior peso: {mais_pesado:.2f} kg")
print(f"Média de altura: {media_altura:.2f} m")
print(f"Média de IMC: {media_imc:.2f}")
print(f"Porcentagem de sexo masculino: {porcentual_masculino:.2f}%")
print(f"Porcentagem de sexo feminino: {porcentual_feminino:.2f}%")
