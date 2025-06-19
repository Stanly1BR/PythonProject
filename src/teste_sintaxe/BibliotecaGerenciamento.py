

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

def menuLivro():
    print("=======================")
    print("======MENU LIVRO======")
    print("========================")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")

while True:

    livros = [{
        "Titulo": "O livro 1",
        "Autor":"",
        "Data_publi":""
    }]
    usuarios = []

    menu()
    opcao = int(input())

    if opcao == 0:
        break

    if opcao == 1:
        menuUsuario()
        opcaoUsuario = int(input())

        if opcaoUsuario == 1:
            print("Cadastrando usuario")
        elif opcaoUsuario == 2:
            print("Listando usuarios")
        elif opcaoUsuario == 3:
            print("Excluindo usuario")



    elif opcao == 2:
        menuLivro()
        opcaoLivro = int(input())

