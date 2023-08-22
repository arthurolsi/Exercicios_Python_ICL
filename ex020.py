import random
aluno1 = str(input("Insira o primeiro aluno"))
aluno2 = str(input("Insira o segundo aluno"))
aluno3 = str(input("Insira o terceiro aluno"))
aluno4 = str(input("Insira o quarto aluno"))

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print("A ordem será: {}".format(alunos))
