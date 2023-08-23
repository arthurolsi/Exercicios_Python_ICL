frase = str("   Bom vídeo batata")
print(frase[4:9])

print("A frase tem {} caracteres".format(len(frase)))  # tamanho

print(frase.count('o'))  # conta qnts 'o' a frase tem

print(frase.find('batata'))  # procura a frase entre aspas ##########

print("batata" in frase)  # operador

print(frase.replace('batata', "melon"))  # troca
print(frase)

print(frase.upper())  # maiusculo

print(frase.lower())  # minusculo

print(frase.capitalize())  # tudo minusculo menos a primeira letra

print(frase.title())  # quebra as palavras e coloca maiusculo

print(frase.strip())  # remove os espaços inúteis --> rstrip Direita e lstrip Esquerda

print(frase.split())  # divide as palavras e refaz os indexs

print('-'.join(frase))  # junção
