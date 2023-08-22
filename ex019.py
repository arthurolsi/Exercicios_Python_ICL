import random
aluno1 = input("Insira o primeiro aluno")
aluno2 = input("Insira o segundo aluno")
aluno3 = input("Insira o terceiro aluno")
aluno4 = input("Insira o quarto aluno")

alunos = [aluno1, aluno2, aluno3, aluno4]

print("O aluno escolhido foi o/a {}".format(random.choice(alunos)))