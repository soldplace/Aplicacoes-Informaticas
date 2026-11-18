produto = {
    "nome": "Computador portátil",
    "referência": 1,
    "preço": 2000,
    "quantidade": 13
}
print("Nome: ", produto.get("nome"))
print("Preço: ", produto.get("preço"))

produto["preço"] = 2500
produto["quantidade"] = 2
produto.update({"categoria": "Eletrónicos"})

for a in produto:
    print(a, ":", produto.get(a))

if "referência" in produto.keys():
    print("A referência está presente")