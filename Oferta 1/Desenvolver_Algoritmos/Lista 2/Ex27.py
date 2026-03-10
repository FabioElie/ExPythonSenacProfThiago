lado_A = int(input("Digite o lado A: "))
lado_B = int(input("Digite o lado B: "))
lado_C = int(input("Digite o lado C: "))

if lado_A<(lado_B+lado_C) and lado_B<(lado_A+lado_C) and lado_C<(lado_B+lado_A):
    if(lado_A == lado_B == lado_C):
        print("Esse triangulo é equilátero")


    elif lado_A != lado_B and lado_A != lado_C and lado_B != lado_C:
        print("Esse triangulo é escaleno")

    elif(lado_A == lado_B or lado_A == lado_C or lado_B == lado_C):
        print("Esse triangulo é isósceles")

else:
    print("Não é um triangulo!")
