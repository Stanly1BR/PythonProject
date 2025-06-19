# Comentários de uma linha começam com um símbolo de cerquilha (hashtag).

""" Strings multilinha podem ser escritas
    usando três aspas, e são frequentemente usadas
    como documentação.
"""

####################################################
## 1. Tipos de Dados Primitivos e Operadores
####################################################

# Você tem números
3  # => 3

# Matemática funciona como você esperaria
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Divisão inteira arredonda para negativo infinito
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0  # também funciona com floats
-5.0 // 3.0  # => -2.0

# O resultado da divisão é sempre um float
10.0 / 3  # => 3.3333333333333335

# Operação módulo
7 % 3   # => 1
# i % j tem o mesmo sinal que j, diferente de C
-7 % 3  # => 2

# Exponenciação (x**y, x elevado à y-ésima potência)
2**3  # => 8

# Forçar precedência com parênteses
1 + 3 * 2    # => 7
(1 + 3) * 2  # => 8

# Valores booleanos são primitivos (Nota: a capitalização)
True   # => True
False  # => False

# Negar com not
not True   # => False
not False  # => True

# Operadores Booleanos
# Note que "and" e "or" são sensíveis a maiúsculas/minúsculas
True and False  # => False
False or True   # => True

# True e False são na verdade 1 e 0 mas com palavras-chave diferentes
True + True  # => 2
True * 8     # => 8
False - 5    # => -5

# Operadores de comparação olham para o valor numérico de True e False
0 == False   # => True
2 > True     # => True
2 == True    # => False
-5 != False  # => True

# None, 0, e strings/listas/dicionários/tuplas/conjuntos vazios todos avaliam para False.
# Todos outros valores são True
bool(0)      # => False
bool("")     # => False
bool([])     # => False
bool({})     # => False
bool(())     # => False
bool(set())  # => False
bool(4)      # => True
bool(-6)     # => True

# Usar operadores lógicos booleanos em inteiros os converte para booleanos para avaliação,
# mas seu valor não convertido é retornado. Não confunda com bool(ints) e operadores
# bitwise and/or (&,|)
bool(0)   # => False
bool(2)   # => True
0 and 2   # => 0
bool(-5)  # => True
bool(2)   # => True
-5 or 0   # => -5

# Igualdade é ==
1 == 1  # => True
2 == 1  # => False

# Desigualdade é !=
1 != 1  # => False
2 != 1  # => True

# Mais comparações
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Verificando se um valor está em um intervalo
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Encadeamento torna isso mais bonito
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is verifica se duas variáveis referem-se ao mesmo objeto, mas == verifica
# se os objetos apontados têm os mesmos valores.
a = [1, 2, 3, 4]  # Aponta a para uma nova lista, [1, 2, 3, 4]
b = a             # Aponta b para o que a está apontando
b is a            # => True, a e b referem-se ao mesmo objeto
b == a            # => True, os objetos de a e b são iguais
b = [1, 2, 3, 4]  # Aponta b para uma nova lista, [1, 2, 3, 4]
b is a            # => False, a e b não referem-se ao mesmo objeto
b == a            # => True, os objetos de a e b são iguais

# Strings são criadas com " ou '
"Isto é uma string."
'Isto também é uma string.'

# Strings podem ser somadas
"Olá " + "mundo!"  # => "Olá mundo!"
# Strings literais (mas não variáveis) podem ser concatenadas sem usar '+'
"Olá " "mundo!"    # => "Olá mundo!"

# Uma string pode ser tratada como uma lista de caracteres
"Olá mundo!"[0]  # => 'O'

# Você pode encontrar o comprimento de uma string
len("Isto é uma string")  # => 16

# Desde Python 3.6, você pode usar f-strings ou strings literais formatadas.
nome = "Reiko"
f"Ela disse que seu nome é {nome}."  # => "Ela disse que seu nome é Reiko."
# Qualquer expressão Python válida dentro dessas chaves é retornada para a string.
f"{nome} tem {len(nome)} caracteres de comprimento."  # => "Reiko tem 5 caracteres de comprimento."

# None é um objeto
None  # => None

# Não use o símbolo de igualdade "==" para comparar objetos com None
# Use "is" ao invés. Isso verifica igualdade de identidade do objeto.
"etc" is None  # => False
None is None   # => True

####################################################
## 2. Variáveis e Coleções
####################################################

# Python tem uma função print
print("Eu sou Python. Prazer em conhecê-lo!")  # => Eu sou Python. Prazer em conhecê-lo!

# Por padrão a função print também imprime uma nova linha no final.
# Use o argumento opcional end para mudar a string final.
print("Olá, Mundo", end="!")  # => Olá, Mundo!

# Forma simples de obter dados de entrada do console
input_string_var = input("Entre com alguns dados: ")  # Retorna os dados como string

# Não há declarações, apenas atribuições.
# Convenção no nome de variáveis é estilo snake_case
alguma_var = 5
alguma_var  # => 5


# if pode ser usado como uma expressão
# Equivalente ao operador ternário '?:' de C
"oba!" if 0 > 1 else "opa!"  # => "opa!"

# Listas armazenam sequências
li = []
# Você pode começar com uma lista pré-preenchida
outra_li = [4, 5, 6]

# Adicionar coisas ao final de uma lista com append
li.append(1)    # li agora é [1]
li.append(2)    # li agora é [1, 2]
li.append(4)    # li agora é [1, 2, 4]
li.append(3)    # li agora é [1, 2, 4, 3]
# Remover do final com pop
li.pop()        # => 3 e li agora é [1, 2, 4]
# Vamos colocar de volta
li.append(3)    # li agora é [1, 2, 4, 3] novamente.

# Acessar uma lista como você faria com qualquer array
li[0]   # => 1
# Olhar para o último elemento
li[-1]  # => 3

# Tentar acessar fora dos limites levanta um IndexError
li[4]  # Levanta um IndexError

# Você pode olhar intervalos com sintaxe de slice.
# O índice inicial é incluído, o final não
# (É um intervalo fechado/aberto para os matemáticos)
li[1:3]   # Retorna lista do índice 1 ao 3 => [2, 4]
li[2:]    # Retorna lista começando do índice 2 => [4, 3]
li[:3]    # Retorna lista do início até o índice 3 => [1, 2, 4]
li[::2]   # Retorna lista selecionando elementos com passo 2 => [1, 4]
li[::-1]  # Retorna lista em ordem reversa => [3, 4, 2, 1]
# Use qualquer combinação para fazer slices avançados
# li[início:fim:passo]

# Faça uma cópia de uma camada usando slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] mas (li2 is li) resultará em falso.

# Remova elementos arbitrários com "del"
del li[2]  # li agora é [1, 2, 3]

# Remova a primeira ocorrência de um valor
li.remove(2)  # li agora é [1, 3]
li.remove(2)  # Levanta um ValueError pois 2 não está na lista

# Insira um elemento em um índice específico
li.insert(1, 2)  # li agora é [1, 2, 3] novamente

# Obtenha o índice do primeiro item encontrado correspondente ao argumento
li.index(2)  # => 1
li.index(4)  # Levanta um ValueError pois 4 não está na lista

# Você pode somar listas
# Nota: valores para li e para outra_li não são modificados.
li + outra_li  # => [1, 2, 3, 4, 5, 6]

# Concatenar listas com "extend()"
li.extend(outra_li)  # Agora li é [1, 2, 3, 4, 5, 6]

# Verificar existência em uma lista com "in"
1 in li  # => True

# Examinar o comprimento com "len()"
len(li)  # => 6

# Tuplas são como listas mas são imutáveis.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Levanta um TypeError

# Note que uma tupla de tamanho um tem que ter uma vírgula depois do último elemento mas
# tuplas de outros tamanhos, mesmo zero, não precisam.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# Você pode fazer a maioria das operações de lista em tuplas também
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True

# Você pode desempacotar tuplas (ou listas) em variáveis
a, b, c = (1, 2, 3)  # a agora é 1, b agora é 2 e c agora é 3
# Você também pode fazer desempacotamento estendido
a, *b, c = (1, 2, 3, 4)  # a agora é 1, b agora é [2, 3] e c agora é 4
# Tuplas são criadas por padrão se você omitir os parênteses
d, e, f = 4, 5, 6  # tupla 4, 5, 6 é desempacotada em variáveis d, e e f
# respectivamente tal que d = 4, e = 5 e f = 6
# Agora veja como é fácil trocar dois valores
e, d = d, e  # d agora é 5 e e agora é 4

# Dicionários armazenam mapeamentos de chaves para valores
dicionario_vazio = {}
# Aqui está um dicionário pré-preenchido
dicionario_preenchido = {"um": 1, "dois": 2, "três": 3}

# Note que chaves para dicionários têm que ser tipos imutáveis. Isto é para garantir que
# a chave pode ser convertida para um valor hash constante para buscas rápidas.
# Tipos imutáveis incluem ints, floats, strings, tuplas.
dicionario_invalido = {[1,2,3]: "123"}  # Levanta TypeError: tipo não hasheável: 'list'
dicionario_valido = {(1,2,3):[1,2,3]}   # Valores podem ser de qualquer tipo, entretanto.

# Procure valores com []
dicionario_preenchido["um"]  # => 1

# Obtenha todas as chaves como um iterável com "keys()". Precisamos envolver a chamada em list()
# para transformar em lista. Falaremos sobre