produtos = [
    {"codigo": 1, "nome": "Arroz", "preco": 25.90, "estoque": 50},
    {"codigo": 2, "nome": "Feijão", "preco": 8.50, "estoque": 80},
    {"codigo": 3, "nome": "Óleo", "preco": 7.20, "estoque": 40}
]

clientes = [{"cpf": "12345678901", "nome": "Fabio", "email": "fabio@email.com", "fone": "67999998888", "cidade": "Campo Grande"}]
carrinho = []

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Produtos")
    print("2 - Clientes")
    print("3 - Carrinho / Venda")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")



    if opcao == "1":
        while True:
            print("\n--- MENU PRODUTOS ---")
            print("1 - Cadastrar produto")
            print("2 - Listar produtos")
            print("3 - Atualizar produto")
            print("4 - Excluir produto")
            print("0 - Voltar")

            op_prod = input("Opção: ")

            if op_prod == "1":
                codigo = int(input("Código: "))

                existe = False
                for p in produtos:
                    if p["codigo"] == codigo:
                        existe = True

                if existe:
                    print("❌ Código já existente.")
                else:
                    nome = input("Nome: ")
                    preco = float(input("Preço: "))
                    estoque = int(input("Estoque: "))
                    produtos.append({
                        "codigo": codigo,
                        "nome": nome,
                        "preco": preco,
                        "estoque": estoque
                    })
                    print("✅ Produto cadastrado com sucesso!")

            elif op_prod == "2":
                print("\n--- PRODUTOS CADASTRADOS ---")
                for p in produtos:
                    print(f"Código: {p['codigo']} | Nome: {p['nome']} | "
                          f"Preço: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")

            elif op_prod == "3":
                codigo = int(input("Informe o código do produto: "))
                encontrado = False

                for p in produtos:
                    if p["codigo"] == codigo:
                        encontrado = True
                        print("1 - Atualizar nome")
                        print("2 - Atualizar preço")
                        print("3 - Atualizar estoque")
                        escolha = input("Escolha: ")

                        if escolha == "1":
                            p["nome"] = input("Novo nome: ")
                        elif escolha == "2":
                            p["preco"] = float(input("Novo preço: "))
                        elif escolha == "3":
                            p["estoque"] = int(input("Novo estoque: "))

                        print("✅ Produto atualizado!")

                if not encontrado:
                    print("❌ Produto não encontrado.")

            elif op_prod == "4":
                codigo = int(input("Código do produto: "))
                removido = False

                for p in produtos:
                    if p["codigo"] == codigo:
                        produtos.remove(p)
                        removido = True
                        print("✅ Produto removido.")

                if not removido:
                    print("❌ Produto não encontrado.")

            elif op_prod == "0":
                break




    elif opcao == "2":
        while True:
            print("\n--- MENU CLIENTES ---")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Atualizar cliente")
            print("4 - Excluir cliente")
            print("0 - Voltar")

            op_cli = input("Opção: ")

            if op_cli == "1":
                cpf = input("CPF: ")
                nome = input("Nome: ")
                email = input("Email: ")
                fone = input("Telefone: ")
                cidade = input("Cidade: ")

                clientes.append({
                    "cpf": cpf,
                    "nome": nome,
                    "email": email,
                    "fone": fone,
                    "cidade": cidade
                })
                print("✅ Cliente cadastrado!")

            elif op_cli == "2":
                print("\n--- CLIENTES ---")
                for c in clientes:
                    print(f"CPF: {c['cpf']} | Nome: {c['nome']} | "
                          f"Email: {c['email']} | Fone: {c['fone']} | Cidade: {c['cidade']}")

            elif op_cli == "3":
                cpf = input("Informe o CPF: ")
                encontrado = False

                for c in clientes:
                    if c["cpf"] == cpf:
                        encontrado = True
                        c["nome"] = input("Novo nome: ")
                        c["email"] = input("Novo email: ")
                        c["fone"] = input("Novo telefone: ")
                        c["cidade"] = input("Nova cidade: ")
                        print("✅ Cliente atualizado!")

                if not encontrado:
                    print("❌ Cliente não encontrado.")

            elif op_cli == "4":
                cpf = input("CPF do cliente: ")
                removido = False

                for c in clientes:
                    if c["cpf"] == cpf:
                        clientes.remove(c)
                        removido = True
                        print("✅ Cliente removido.")

                if not removido:
                    print("❌ Cliente não encontrado.")

            elif op_cli == "0":
                break






    elif opcao == "3":
        carrinho = []

        while True:
            print("\n--- CARRINHO ---")
            print("1 - Adicionar produto")
            print("2 - Finalizar compra")
            print("0 - Cancelar")

            op_car = input("Opção: ")

            if op_car == "1":
                codigo = int(input("Código do produto: "))
                quantidade = int(input("Quantidade: "))

                encontrado = False
                for p in produtos:
                    if p["codigo"] == codigo:
                        encontrado = True
                        if p["estoque"] >= quantidade:
                            subtotal = p["preco"] * quantidade
                            carrinho.append({
                                "codigo": codigo,
                                "nome": p["nome"],
                                "preco": p["preco"],
                                "quantidade": quantidade,
                                "subtotal": subtotal
                            })
                            p["estoque"] -= quantidade
                            print("✅ Produto adicionado ao carrinho.")

                            print("\n--- ITENS NO CARRINHO ---")
                            for item in carrinho:
                                print(f"{item['nome']} | R$ {item['preco']:.2f} | "
                                    f"Qtd: {item['quantidade']} | Subtotal: R$ {item['subtotal']:.2f}")
                        else:
                            print("❌ Estoque insuficiente.")

                if not encontrado:
                    print("❌ Produto não encontrado.")


            elif op_car == "2":
                total = 0
                print("\n--- RESUMO DA COMPRA ---")
                for item in carrinho:
                    print(f"{item['nome']} | R$ {item['preco']:.2f} | "
                          f"Qtd: {item['quantidade']} | Subtotal: R$ {item['subtotal']:.2f}")
                    total += item["subtotal"]

                imposto_nacional = total * 0.05
                imposto_estadual = total * 0.08
                imposto_municipal = total * 0.12

                print(f"\nImposto Nacional (5%): R$ {imposto_nacional:.2f}")
                print(f"Imposto Estadual (8%): R$ {imposto_estadual:.2f}")
                print(f"Imposto Municipal (12%): R$ {imposto_municipal:.2f}")

                print(f"\nTOTAL DA COMPRA: R$ {total + imposto_nacional + imposto_estadual + imposto_municipal:.2f}")
                break

            elif op_car == "0":
                print("❌ Compra cancelada.")
                break


    elif opcao == "0":
        print("👋 Sistema encerrado.")
        break

    else:
        print("❌ Opção inválida.")
