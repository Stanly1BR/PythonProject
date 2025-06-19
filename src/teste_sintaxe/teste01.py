notas = []

for c in range(0, 2):
    nota = int(input("Qual sua nota? "))
    notas.append(nota)  # adiciona a nota na lista

media = sum(notas)  / len(notas)
print(f"A média das notas é: {media}")