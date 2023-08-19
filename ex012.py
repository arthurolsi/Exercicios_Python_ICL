preco = float(input("Informe o preço do produto"))
precoDesconto = preco - (preco * 5 / 100)

print("Com um desconto de 5% o valor final fica em {:.2f} reais".format(precoDesconto))
