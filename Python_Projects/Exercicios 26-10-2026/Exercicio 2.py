import random

temperaturas = []
maioresqueamedia = 0

for i in range(7):
    temperaturas.append(random.randint(10, 30))

temperaturas.sort()
print(temperaturas)
temperaturamedia = sum(temperaturas) / len(temperaturas)
print("Temperaturas Médias: ", round(temperaturamedia, 2))
for i in temperaturas:
    if i > temperaturamedia:
        maioresqueamedia += 1

print("Dias superiores à media: ", maioresqueamedia)