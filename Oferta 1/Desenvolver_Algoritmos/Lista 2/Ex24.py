base1 = float(input("Digite a primeira base do trapézio: "))
base2 = float(input("Digite a segunda base do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))

if (base1<0 or base2<0):
    print("Base com numero menor que 0 são invalidas")
else:
    A = ((base1 + base2) * altura)/2

    print(f"O trapézio possui uma área de {((base1 + base2) * altura)/2}")