from Animal import Animal
from Cachorro import Cachorro
from Gato import Gato
from Peixe import Peixe

listaDeAnimais = []
print("-" * 30)
print("Sistema de Animais")
print("-" * 30)

while True:

    print("\nQual animal deseja cadastrar?")
    op = int(input("1-Cachorro 2-Gato 3-Peixe 4-Genérico 5-Listar Animais 0-Sair: "))

    if op == 1:
        nome = input("Digite o nome do cachorro: ")
        cor = input("Digite a cor do cachorro: ")
        raca = input("Digite a raça do cachorro: ")
        rabo = input("O cachorro tem rabo? (s/n): ")
        if rabo.lower() == "n":
            rabo = False
        else:
            rabo = True

        cachorro = Cachorro(nome, cor, raca, rabo)
        listaDeAnimais.append(cachorro)
        print("__" * 30)
        print(cachorro.info())
        print(cachorro.mover())
        print(cachorro.latir())

    elif op == 2:
        nome = input("Digite o nome do gato: ")
        cor = input("Digite a cor do gato: ")
        raca = input("Digite a raça do gato: ")

        gato = Gato(nome, cor, raca)
        listaDeAnimais.append(gato)

        print("__" * 30)
        print(gato.info())
        print(gato.mover())
        print(gato.miar())

    elif op == 3:
        nome = input("Digite o nome do peixe: ")
        cor = input("Digite a cor do peixe: ")
        tipo = input("Digite o tipo do peixe: ")

        peixe = Peixe(nome, cor, tipo)
        listaDeAnimais.append(peixe)
        print("__" * 30)
        print(peixe.info())
        print(peixe.mover())
        print(peixe.fazGluGlu())

    elif op == 4:
        nome = input("Digite o nome do animal: ")
        cor = input("Digite a cor do animal: ")

        animalGenerico = Animal(nome, cor)
        listaDeAnimais.append(animalGenerico)
        print("__" * 30)
        print(animalGenerico.info())
        print(animalGenerico.mover())
        print(animalGenerico.fazerSom())

    elif op == 5:
        print("__" * 30)
        print("Lista de Animais Cadastrados:")
        for animal in listaDeAnimais:
            print(animal.info())

    elif op == 0:
        print("__" * 30)
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")
