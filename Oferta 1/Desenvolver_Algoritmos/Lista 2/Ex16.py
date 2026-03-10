
horas_trabalhadas = int(input("Digite quantas horas o funcionário trabalhou: "))

salario = horas_trabalhadas *40.5

if (salario>2500):
    print(f"O salario de R${salario} possui imposto no valor de R${salario * 0.11}, então será pago ao funcionário a quantia de R${salario * 0.89}")
else:
    print(f"O salário é de R${salario}")