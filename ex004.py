algo = input("Digite algo")

print("{} O tipo desse valor é: {}. É um núemro? {} // uma letra? {} // ascii? {} // um decimal? {} // um dígito? {} // um texto em minúsculo? {} // um texto em maiúsculo? {} // espaço? {}.".format(algo, type(algo), algo.isnumeric(), algo.isalpha(), algo.isascii(), algo.isdecimal(), algo.isdigit(), algo.islower(), algo.isupper(), algo.isspace()))
