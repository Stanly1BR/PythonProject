import os


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



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastrar(lista, campos):
    item = {}
    for campo in campos:
        item[campo] = input(f"Digite o {campo}: ")
    lista.append(item.copy())

def listar(lista):
    for item in lista:
        print(item)

def excluir(lista, buscarpor, chave):

    encontrado = False
    for item in lista:
        if item[chave] == buscarpor:
            lista.remove(item)
            print("Excluido com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print("Item não encontrado no sistema")

livros = list()
usuarios = list()
livro = dict()
usuario = dict()

while True:

    limpar_tela()
    menu()
    opcao = 0

    try:
        opcao = int(input())
        if opcao == 0:
            break
        if opcao < 0 or opcao >2:
            print("Por favor, digite uma opção valida segundo o menu")
            continue

    except ValueError:
        print("Por favor, digitir uma opção  segundo o menu")

    if opcao == 1:
        try:
            limpar_tela()
            menu_usuario()
            opcaoUsuario = int(input())
            if opcaoUsuario < 1 or opcaoUsuario > 4:
                print("Por favor, digite uma opção valida segundo o menu")
                continue

            if opcaoUsuario == 1:
                print("Cadastrando usuario")
                print("========================")
                cadastrar(usuarios, ["nome", "email", "senha"])

            elif opcaoUsuario == 2:
                print("Listando usuarios")
                print("========================")
                listar(usuarios)

            elif opcaoUsuario == 3:
                print("Excluindo usuario")
                print("========================")
                excluir(usuarios, str(input("Qual o nome do usuario que deseja excluir?")), "nome")

        except ValueError:
            print("Por favor digite uma opção valida, conforme o menu")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")



    elif opcao == 2:
        try:
            limpar_tela()
            menu_livro()
            opcaoLivro = int(input())
            if opcaoLivro < 1 or opcaoLivro > 4:
                print("Por favor, digite uma opção valida segundo o menu")
                continue

            if opcaoLivro == 1:
                print("Cadastrando livro")
                print("========================")
                cadastrar(livros, ["titulo", "autor", "genero"])

            elif opcaoLivro == 2:
                print("Listando livros")
                print("========================")
                listar(livros)

            elif opcaoLivro == 3:
                print("Excluindo livro")
                print("========================")
                excluir(livros, str(input("Qual o titulo do livro que deseja excluir?")), "titulo")

        except ValueError:
            print("Por favor digite uma opção valida, conforme o menu")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")