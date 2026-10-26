import random

lista = random.sample(range(1, 51), 3)
if lista[0] == lista[1] or lista[0] == lista[2] or lista[1] == lista[2]:
    lista = random.sample(range(1, 51), 3)
lista.sort()
print("Lista: ", lista)
input = int(input("Inserir valor para verificar: "))
if input in lista:
    print("Valor sorteado!")
else:
    print("Valor não sorteado")
