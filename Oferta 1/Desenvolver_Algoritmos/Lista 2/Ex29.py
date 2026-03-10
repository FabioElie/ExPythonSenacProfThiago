idade = int(input("Qual a sua idade? "))
tempo = int(input("Quantos anos de serviço você possui? "))

if(idade>=65 or tempo>=30 or (idade>=60 and tempo>=25)):
    print("Pode se aposentar!")
else:
    print("Ainda não pode se aposentar!")