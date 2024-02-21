# Leia um valor inteiro do termina e imprima um quadrado com
# tantas linhas e tantas colunas quanto for o número informado 

# *****
# *****
# *****
# *****
# *****
# *****

# Ler um valor inteiro do terminal
n = int(input("Digite um valor inteiro: "))

# Imprimir o quadrado com dois loops
for i in range(n):
    for j in range(n):
        print('* ', end='')
    print()
