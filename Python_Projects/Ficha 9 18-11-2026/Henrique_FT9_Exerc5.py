alunos = {
    1: {"nome": "Ana", "notas": [15, 16, 18]},
    2: {"nome": "João", "notas": [12, 14, 16]},
    3: {"nome": "Pedro", "notas": [10, 13, 15]}
}
for a in alunos.values():
    print("Nome: ", a.get("nome"))
    print("Notas: ", a.get("notas"))

medias = {}
for v in alunos.values():
    notas = v.get("notas")
    media = sum(notas) / len(notas)
    print("A média do(a) aluno(a)" , v.get("nome"), "é: " , round(media, 2))
    medias.update({str(v.get("nome")): round(media, 2)})
print("O aluno com a melhor média foi o(a): ", max(medias, key=medias.get))