aluna = ("Maria", "17", "Informática", "16")

print(f"Nome: {aluna[0]}\n"
      f"Idade: {aluna[1]}\n"
      f"Curso: {aluna[2]}\n"
      f"Classificação: {aluna[3]}\n")
print("Número de elementos: ", len(aluna))
for a in aluna:
    print(a)

nome = aluna[0]
idade = aluna[1]
curso = aluna[2]
nota = aluna[3]

print("Nome: ", nome)
print("Idade: ", idade)
print("Curso: ", curso)
print("Nota: ", nota)

# Questão de reflexão: o que acontece se tentares executar aluno[0] = "Mariana"? Explica porquê.
# Resposta: o python não aceita o valor porque a tuple não suposta alterações.