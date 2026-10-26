import random

lancamentos = []

quandidadede6 = 0

for i in range(10):
    lancamentos.append(random.randint(1,6))

print(lancamentos)

for i in lancamentos:
    if i == 6:
        quandidadede6 += 1

print("Vezes que saiu o 6: ", quandidadede6)
print("Máximo: ", max(lancamentos))
print("Mínimo: ", min(lancamentos))