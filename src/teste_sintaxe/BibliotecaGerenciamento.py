def menu() -> None:
    print("=======================")
    print("========MENU============")
    print("========================")
    print("1 - Usuario")
    print("2 - Livro")
    print("0 - Sair")
    print("========================")
    print("Digite a opção:")

def menu_usuario() -> None:
    print("=======================")
    print("======MENU USUARIO====")
    print("========================")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Voltar")
    print("========================")
    print("Digite a opção:")

def menu_livro() -> None:
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
usuario = dict()

while True:

    menu()
    opcao = int(input())

    if opcao == 0:
        break

    if opcao == 1:
        menu_usuario()
        opcaoUsuario = int(input())

        if opcaoUsuario == 1:
            print("Cadastrando usuario")
            print("========================")
            usuario["nome"] = str(input("Digite o nome de usuario: "))
            usuario["telefone"] = str(input("Digite o telefone de usuario: "))
            usuarios.append(usuario.copy())

        elif opcaoUsuario == 2:
            print("Listando usuarios")
            print("========================")
            for usuario in usuarios:
                print(usuario)

        elif opcaoUsuario == 3:
            print("Excluindo usuario")
            print("========================")
            nome = str(input("Qual o nome do usuario que deseja excluir?"))

            encontrou = False
            for usuario in usuarios:
                if usuario["nome"] == nome:
                    usuario.remove(usuario)
                    print("Usuario excluido com sucesso!")
                    encontrou = True
                    break
            if not encontrou:
                print("Usuario não encontrado no sistema")



    elif opcao == 2:
        menu_livro()
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