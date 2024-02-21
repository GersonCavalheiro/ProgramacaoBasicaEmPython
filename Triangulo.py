# Leia um valor inteiro do termina e imprima um triângulo com
# tantas linhas quanto for o número informado e, na primeira linha
# um asterisco, na segunda dois asteriscos até chegar na linha
# final, com tantos asteriscos quanto o número informado

# *
# **
# ***
# ****
# *****
# ******
# *******

# Ler um valor inteiro do terminal
n = int(input("Digite um valor inteiro: "))

# Imprimir a imagem
for linha in range(1, n + 1):
    for coluna in range(1, linha+1):
        print('* ', end='')
    print()
