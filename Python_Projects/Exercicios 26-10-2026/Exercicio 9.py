import random

vendas = []

for i in range(30):
    vendas.append(random.randint(100, 1000))

faturacaototal = sum(vendas)
vendamedia = sum(vendas) / len(vendas)
melhordia = vendas.index(max(vendas))

boasvendas = []
for i in vendas:
    if i > 700:
        boasvendas.append(vendas.index(i))

vendasdecrescente = vendas.copy()
vendasdecrescente.sort(reverse=True)

print("Vendas: ", vendas)
print("Faturação total: ", faturacaototal)
print("Dia com maior faturação: ", melhordia)
print("Dias em que as vendas ultrapassaram os 700€: ", boasvendas)
print("Vendas por ordem descrescente: ", vendasdecrescente)