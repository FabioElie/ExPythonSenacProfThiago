letra = str(input("Digite M - Matutino ou V - Vespertino ou N - Noturno ")).upper()

if(letra == "M"):
    print("Bom dia!")
elif(letra == "V"):
    print("Boa Tarde!")
elif(letra == "N"):
    print("Boa Noite!")
else:
    print("Valor Invalido")