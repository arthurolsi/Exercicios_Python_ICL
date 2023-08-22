import math
angulo = float(input("Insira um ângulo"))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(" Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}".format(seno, cosseno, tangente))
