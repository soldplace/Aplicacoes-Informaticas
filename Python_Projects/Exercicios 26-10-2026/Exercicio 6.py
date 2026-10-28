import random

deslocamentospossiveis = [-1, 0, 1]

deslocamentos = []
for i in range(15):
    a = random.choice(deslocamentospossiveis)
    deslocamentos.append(a)

final = sum(deslocamentos)
print("Deslocamento Final: ", final)

direita = 0
esquerda = 0
parado = 0

for deslocamento in deslocamentos:
    if deslocamento == 0:
         parado += 1
    # PERGUNTAR AO STOR QUAL DOS VALORES (-1 E 1) É A ESQUERDA E A DIREITA
    if deslocamento == -1:
        direita += 1
    if deslocamento == 1:
        esquerda += 1
print("Deslocamento Direita: ", direita)
print("Deslocamento Esquerda: ", esquerda)
print("Parado: ", parado)

posicoes = []
posicao = 0
for deslocamento in deslocamentos:
    posicao += deslocamento
    posicoes.append(posicao)
print("Histórico de posições: ", posicoes)