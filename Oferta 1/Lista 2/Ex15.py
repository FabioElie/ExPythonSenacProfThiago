nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if(nota1<0 or nota2<0):
    print("Nota Invalida: Menor que Zero!")
elif(nota1>10 or nota2>10):
    print("Nota Invalida: Maior que 10!")
else:
    print(f"A média das notas {nota1} e {nota2} é de {(nota1+nota2)/2:.2f}")