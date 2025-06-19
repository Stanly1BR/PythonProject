def menu():
    print("=======================")
    print("========MENU============")
    print("========================")
    print("1 - Usuario")
    print("2 - Livro")
    print("0 - Sair")
    print("========================")
    print("Digite a opção:")

def menuUsuario():
    print("=======================")
    print("======MENU USUARIO====")
    print("========================")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Voltar")
    print("========================")
    print("Digite a opção:")

def menuLivro():
    print("=======================")
    print("======MENU LIVRO======")
    print("========================")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Voltar")
    print("========================")
    print("Digite a opção:")

livros = list()
usuarios = list()
livro = dict()
usuarios = dict()

while True:

    menu()
    opcao = int(input())

    if opcao == 0:
        break

    if opcao == 1:
        menuUsuario()
        opcaoUsuario = int(input())

        if opcaoUsuario == 1:
            print("Cadastrando usuario")
            print("========================")

        elif opcaoUsuario == 2:
            print("Listando usuarios")
            print("========================")

        elif opcaoUsuario == 3:
            print("Excluindo usuario")
            print("========================")



    elif opcao == 2:
        menuLivro()
        opcaoLivro = int(input())

        if opcaoLivro == 1:
            print("Cadastrando livro")
            livro["titulo"] = str(input("Digite o titulo do livro: "))
            livro["autor"] = str(input("Digite o autor do livro: "))
            livro["dataPublicacao"] = str(input("Digite a data de publicação: "))
            livros.append(livro.copy())

        elif opcaoLivro == 2:
            print("Listando livros")
            print("========================")
            for livro in livros:
                print(livro)

        elif opcaoLivro == 3:
            print("Excluindo livro")
            print("========================")
            titulo = str(input("Qual o titulo do livro que deseja excluir?"))

            encontrou = False
            for livro in livros:
                if livro["titulo"] == titulo:
                    livros.remove(livro)
                    encontrou = True
                    print("Livro excluido com sucesso!")
                    break

            if not encontrou:
                print("Livro não encontrado no sistema")