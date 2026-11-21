clubes = {
    "Xadrez" : {"André", "Zé", "Carolina"},
    "Luta Livre": {"Tomás", "Sócrates", "Zé", "André"},
    "Vólei": {"Sócrates", "Zé", "Sara"}
}
while True:
    print("\nPrograma dos clubes da escola\n"
          "Escolhe uma das seguintes opções:\n"
          "1 - Apresentar alunos de um clube\n"
          "2 - Adicionar aluno a um clube\n"
          "3 - Identificar alunos inscritos em todos os clubes\n"
          "4 - Apresentar conjunto de todos os alunos incritos em clubes\n"
          "5 - Sair")
    match int(input("Selecionar opção: ")):
        case 1:
            while True:
                clube = str(input(f"Selecione um dos seguintes clubes: {list(clubes.keys())}\n"))
                if clube not in clubes:
                    print("Clube inválido")
                else:
                    print(clubes[clube])
                    break
        case 2:
            while True:
                nome = str(input("Inserir o nome de um aluno a adicionar: "))
                clube = str(input(f"Selecione um dos seguintes clubes onde adicionar o aluno: {set(clubes.keys())}\n"))
                if clube not in clubes:
                    print("Clube inválido")
                elif nome in clubes.get(clube):
                    print(f"O aluno '{nome}' já faz parte do clube {clube}")
                else:
                    c = clubes.get(clube)
                    c.update([nome])
                    break
        case 3:
            print("Alunos inscritos em todos os clubes: ", set.intersection(*[set(nome) for nome in clubes.values()]))
        case 4:
            print("Alunos inscritos em pelo menos 1 clube: ", set.union(*[set(nome) for nome in clubes.values()]))
        case 5:
            break
        case _:
            print("Escolha Inválida!")
