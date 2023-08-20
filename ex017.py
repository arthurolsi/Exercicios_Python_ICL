from math import hypot
catOposto = float(input("Insira o comprimento do cateto oposto"))
catAdjacente= float(input("Insira o comprimento do cateto adjacente"))
hipotenusa = hypot(catOposto, catAdjacente)

print("O valor da hipotenusa é: {:.2f}".format(hipotenusa))
