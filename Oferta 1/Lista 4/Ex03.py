# Crie um programa que determine o mostre os 10 primeiros números pares, considerando 
# números maiores que 0. 
i = 0

while i < 10:
    if i % 2 == 0 and i != 0:
        print(i, "é par")
    
    i += 1
