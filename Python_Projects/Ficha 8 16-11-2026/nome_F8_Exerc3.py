import random

secreto = random.randint(1, 100)
tentativas = 0
def verificar(numero):
    if numero > secreto:
        tentativas += 1
        return "Maior"
    elif numero < secreto:
        tentativas += 1
        return "Menor"
    else:
        return True


print("JOGO - NÙMERO SECRETO\n"
      "Tenta descobrir o número secreto (entre 1 e 100)\n")