import random

def gerarchave():
    numeros = random.sample(range(1, 51), 5)
    numeros.sort()
    estrelas = random.sample(range(1, 12), 2)
    estrelas.sort()
    return numeros, estrelas

chavemestra = gerarchave()

chaverandom = gerarchave()

numerosemcomum = 0
estrelasemcomum = 0
for i in chaverandom[0]:
    if i in chavemestra[0]:
        numerosemcomum += 1

for i in chaverandom[1]:
    if i in chavemestra[1]:
        estrelasemcomum += 1

print("Euromilhões:\n"
      "Nnúmeros: ", chavemestra[0], "\n"
      "Estrelas: ", chavemestra[1], "\n")
print("A sua aposta:\n"
      "Números: ", chaverandom[0], "\n"
      "Estrelas: ", chaverandom[1], "\n")
print("Números certas: ", numerosemcomum, "\n"
      "Estrelas certas: ", estrelasemcomum, "\n")