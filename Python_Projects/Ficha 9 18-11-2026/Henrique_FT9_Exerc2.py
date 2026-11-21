futebol = {"Ana", "João", "Pedro", "Rita"}
natacao = {"João", "Rita", "Carlos", "Marta"}

print("Alunos inscritos em pelo menos uma atividade: ", futebol | natacao)
print("Alunos inscritos nas duas atividades: ", futebol & natacao)
print("Alunos que praticam futebol, mas não natação: ", futebol - natacao)
print("alunos que praticam apenas uma das atividades: ", futebol ^ natacao)