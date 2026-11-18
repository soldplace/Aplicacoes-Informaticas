import random

secreto = random.randint(1, 100)
print(secreto)
tentativas = 0
def verificar(numero):
    if numero > secreto:
        return "Menor"
    elif numero < secreto:
        return "Maior"
    else:
        return None


print("JOGO - NÙMERO SECRETO\n"
      "Tenta descobrir o número secreto (entre 1 e 100)\n")
while True:
    numero = int(input("Inserir número: "))
    if verificar(numero) == "Maior":
        tentativas += 1
        print("Maior")
    elif verificar(numero) == "Menor":
        tentativas += 1
        print("Menor")
    else:
        break
print(secreto, "é o número certo!")
print("Tentativas: ", tentativas)