alunos = {
    1: {"nome": "Ana", "notas": [15, 16, 18]},
    2: {"nome": "João", "notas": [12, 14, 16]},
    3: {"nome": "Pedro", "notas": [10, 13, 15]}
}
for a in alunos.values():
    print("Nome: ", a.get("nome"))
    print("Notas: ", a.get("notas"))


for i in alunos.values():
    media = sum(i.get("notas")) / len(i.get("notas"))
    print("A média do(a) aluno" , i.get("nome"), "é: " , media)
print()