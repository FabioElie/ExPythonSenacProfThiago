def calculaPeixe (kilos):
    if kilos > 50:
        excesso = kilos - 50
        multa = excesso * 4
        print(f"Voce trouxe {kilos}kgs de peixe, excedendo em {excesso}kgs, voce terá que pagar R${multa:.2f} em multa.")
    else:
        print(f"Voce trouxe {kilos}kgs de peixe,não excedendo o limite.")

calculaPeixe(60)