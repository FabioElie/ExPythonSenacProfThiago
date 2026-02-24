salario = float(input("Digite o valor do seu salario: "))
parcela = float(input("Qual o valor maximo da parcela do empréstimo que deseja pagar? "))

print("Empréstimo não concedido!" if ((parcela*100)/salario)>20 else ("Empréstimo concedido!"))