# Entrada e saída de dados
idade = int(input("Digite um sua idade: "))

# Condicional if, elif, else
if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")

# Loop for
for numero in [1, 2, 3, 4, 5]:
    print(numero)

# Loop while
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# break e continue
for numero in [1, 2, 3, 4, 5]:
    if numero == 3:
        break  # sai do loop quando encontra o número 3
    print(numero)

for numero in [1, 2, 3, 4, 5]:
    if numero == 3:
        continue  # pula para a próxima iteração quando encontra o número 3
    print(numero)
