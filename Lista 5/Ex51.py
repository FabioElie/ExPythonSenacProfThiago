votos_jose = 0
votos_joao = 0
votos_maria = 0
votos_ana = 0
votos_nulos = 0
votos_brancos = 0
total_votos = 0

print("""
Códigos dos candidatos:
1 - José | 2 - João | 3 - Maria | 4 - Ana
5 - Voto Nulo | 6 - Voto em Branco
0 - Encerrar votação
""")


while True:
    voto = int(input("Digite o código do candidato: "))

    if voto == 0:
        break
    elif voto == 1:
        votos_jose += 1
        total_votos += 1
    elif voto == 2:
        votos_joao += 1
        total_votos += 1
    elif voto == 3:
        votos_maria += 1
        total_votos += 1
    elif voto == 4:
        votos_ana += 1
        total_votos += 1
    elif voto == 5:
        votos_nulos += 1
        total_votos += 1
    elif voto == 6:
        votos_brancos += 1
        total_votos += 1
    else:
        print("Código inválido!!!")


    perc_nulos = (votos_nulos / total_votos) * 100
    perc_brancos = (votos_brancos / total_votos) * 100

candidatos = {
    "José": votos_jose,
    "João": votos_joao,
    "Maria": votos_maria,
    "Ana": votos_ana
}

vencedor = max(candidatos, key=candidatos.get)



print("\nRESULTADO DA ELEIÇÃO")
print("_"*100)
print(f"O VENCEDOR foi o/a {vencedor} ")
print(f"José: teve  o total de {votos_jose} votos, percentual de votos {(votos_jose /total_votos) * 100:.2f}%")
print(f"João: teve  o total de {votos_joao} votos, percentual de votos {(votos_joao /total_votos) * 100:.2f}%")
print(f"Maria: teve  o total de {votos_maria} votos, percentual de votos {(votos_maria /total_votos) * 100:.2f}%")
print(f"Ana: teve  o total de {votos_ana} votos, percentual de votos {(votos_ana /total_votos) * 100:.2f}%")
print(f"Votos nulos: {votos_nulos}, percentual de votos nulos: {perc_nulos:.2f}%")
print(f"Votos em branco: {votos_brancos}, percentual de votos em branco: {perc_brancos:.2f}%")