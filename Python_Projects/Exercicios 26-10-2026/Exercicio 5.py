import random

notas = []

for i in range(25):
    notas.append(random.randint(0, 20))

print("Notas: ", notas)

media = sum(notas) / len(notas)

print("Média da turma: ", media)

print("Nota máxima: ", max(notas))
print("Nota Mínima: ", min(notas))

negativas = []
positivas = 0
for nota in notas:
    if nota >= 10:
        positivas += 1
    else:
        negativas.append(nota)
print("Notas Positivas: ", positivas)
print("Notas Negativas: ", negativas)