import random

deslocamentospossiveis = [-1, 0, 1]

deslocamentos = []
for i in range(15):
    a = random.choice(deslocamentospossiveis)
    deslocamentos.append(a)

final = sum(deslocamentos)

for deslocamento in deslocamentos:
    if deslocamento == 0:
