import random

def Exercicio1():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if num1 > num2:
        print(f"{num1} é maior que {num2}")
    elif num1 < num2:
        print(f"{num1} é menor que {num2}")
    else:
        print(f"{num1} é igual a {num2}")

def Exercicio2():
    num = int(input("Digite um número para a tabuada: "))
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

def Exercicio3():
    num = int(input("Digite um número para a contagem regressiva: "))

    while num > 0:
        print(num)
        num -= 1

def Exercicio4():
    num = int(input("Digite um número para verificar se é primo: "))
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")

def Exercicio5():
    num = int(input("Digite um número para calcular a soma dos ímpares: "))
    soma = 0

    for i in range(1, num + 1, 2):
        soma += i

    print(f"A soma dos ímpares até {num} é {soma}.")

def Exercicio6():
    numero_aleatorio = random.randint(1, 100)
    tentativa = 0

    while True:
        palpite = int(input("Tente adivinhar o número (entre 1 e 100): "))
        tentativa += 1

        if palpite == numero_aleatorio:
            print(f"Parabéns! Você acertou em {tentativa} tentativas.")
            break
        elif palpite < numero_aleatorio:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

def Exercicio7():
    palavra = input("Digite uma palavra para contar as vogais: ")
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador += 1

    print(f"A palavra '{palavra}' possui {contador} vogais.")

def Exercicio8():
    n = int(input("Digite um número para gerar a sequência de Fibonacci: "))
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def Exercicio9():
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    else:
        print("Operação inválida.")
        return

    print(f"Resultado da operação: {resultado}")

def Exercicio10():
    soma_multiplos = 0

    for i in range(1, 100):
        if i % 3 == 0 or i % 5 == 0:
            soma_multiplos += i

    print(f"A soma dos múltiplos de 3 ou 5 abaixo de 100 é {soma_multiplos}")

# Teste das funções
Exercicio1()
Exercicio2()
Exercicio3()
Exercicio4()
Exercicio5()
Exercicio6()
Exercicio7()
Exercicio8()
Exercicio9()
Exercicio10()
