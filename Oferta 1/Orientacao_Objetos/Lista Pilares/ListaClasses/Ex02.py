# 2 - Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os 
# seguintes atributos:
#  Nome
#  Autor
#  Editora
#  Páginas
#  A classe deve ter o seguintes métodos:
#  Alterar_editora()
#  Listar_qtde_paginas()

class Livro:
    def __init__(self, nome: str, autor: str, editora: str, paginas: int):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora: str) -> None:
        self.editora = nova_editora

    def listar_qtd_paginas(self) -> int:
        return self.paginas


livro1 = Livro("O Alquimista", "Paulo Coelho", "Arqueiro", 300)
print(f"Nome: {livro1.nome}")
print(f"Autor: {livro1.autor}")
print(f"Editora: {livro1.editora}")
print(f"Páginas: {livro1.listar_qtd_paginas()}")
livro1.alterar_editora("Sextante")
print(f"Editora atualizada: {livro1.editora}")
