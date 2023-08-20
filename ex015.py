dias = int(input("Quantos dias você ficou com o carro?"))
valorDias = dias * 60
km = float(input("Quantos Km você rodou com o carro?"))
valorKm = km * 0.15
valorFinal = valorDias + valorKm

print("O total a pagar é {:.2f} reais".format(valorFinal))
