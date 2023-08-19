n1 = int(input("Digite um número para ver sua tabuada"))
indice = 0

for indice in range(11):
    print("{} X {:2} = {}".format(n1, indice, n1 * indice))
    indice + 1
