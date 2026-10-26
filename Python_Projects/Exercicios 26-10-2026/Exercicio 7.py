import random

lancamentos = []

for i in range(1000):
    lancamentos.append(random.randint(1, 6))

numero1, numero2, numero3, numero4, numero5, numero6 = 0, 0, 0, 0, 0, 0

for lancamento in lancamentos:
    match lancamento:
        case 1:
            numero1 += 1
        case 2:
            numero2 += 1
        case 3:
            numero3 += 1
        case 4:
            numero4 += 1
        case 5:
            numero5 += 1
        case 6:
            numero6 += 1

