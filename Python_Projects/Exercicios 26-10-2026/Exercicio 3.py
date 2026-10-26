import random

lista = []

for i in range(100):
    lista.append(random.randint(0, 100))
print("Lista: ", lista)
pares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)
print("Números pares: ", pares)

maiorque50 = []
for i in lista:
    if i > 50:
        maiorque50.append(i)
print("Maiores que 50: ", maiorque50)
lista.sort()
print("Lista por ordem crescente: ", lista)