import random

lista = random.sample(range(1, 51), 5)
print("Lista: ", lista)
input = int(input("Inserir valor para verificar: "))
if input in lista:
    print("Valor sorteado!")
else:
    print("Valor não sorteado")
