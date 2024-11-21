#Desafio 01: Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.
numero = 1
soma = 0

while numero <= 100:
    if numero % 2 == 0:
        soma += numero
    numero += 1
print(f"A soma dos números pares entre 1 e 100 é: {soma}")    

#Desafio 02: Escreva um programa que use um laço while para exibir todos os números ímpares de 1 a 50.
numero = 1
soma = 0

while numero <= 50:
    if numero % 2 != 0:
        soma += numero
    numero += 1
print(f"A soma dos números ímpares entre 1 e 50 é: {soma}")


#Desafio 03: Faça um programa que use um laço while para exibir os primeiros 20 termos da sequência de Fibonacci.
#A regra básica da sequência é que cada novo número, a partir do terceiro termo, é a soma dos dois números anteriores.
num_a = 1
num_b = 0
num_c = 0
contador = 1

print("Os 20 primeiros números de fibonacci são: ")

while contador <= 20:
    num_c = num_a + num_b
    print(num_c)
    num_a = num_b
    num_b = num_c
    contador +=1 

#Desafio 04: Desenvolva um programa que solicite um número ao usuário e use um laço while para calcular o fatorial desse número.
num = int(input("Digite um número: "))
resultado = num

print(f"O fatorial do número {num} é: ")

while num > 1:
    resultado *= (num - 1)
    num -= 1
print(resultado)


#Desafio 01: Crie um programa que solicite dois números ao usuário,representando um intervalo. Use um laço while para exibir todos os números pares dentro desse intervalo.
num = int(input("Por favor, digite um número: "))
num2 = int(input("Por favor, digite outro número: "))
 
print(f"Os números pares dentro do intervalo entre {num} e {num2} são: ")
while num != num2:
    if num < num2:
        num += 1
        if num % 2 == 0 and num < num2:
            print(num)
    else:
        num -= 1
        if num % 2 == 0 and num > num2:
            print(num)

#Desafio 02: Faça um programa que use um laço while para fazer uma contagem regressiva de um número inserido pelo usuário até 0. Durante a contagem, exiba "Número par" para os 
# números pares.

num = int(input("Por favor, insira um número maior que zero."))
if num > 0:
    print("Contagem Regressiva: ")
    while num > 0:
        num -= 1
        if num % 2 == 0:
            print(f"{num} - Número par")
        else:
            print(num)
else:
    print("Número inválido. Por favor, reinicie o programa e digite um número maior que zero.")


#Desafio 03: Escreva um programa que solicite um número ao usuário e use um laço while para somar os dígitos do número até que a soma seja um único dígito.

num = int(input("Por favor, digite um número: "))
soma = 0

while num > 0:
    soma += num % 10
    num = num // 10

print(f"A soma de todos os algarismos do número digitado é: {soma}")
    

#Desafio 04: Crie um programa que solicite um número ao usuário e use um laço while para gerar e exibir a sequência de Collatz até chegar ao número 1.
#Se Par = divide por 2
#Se impar = 3 * x + 1

num = int(input("Digite um número e veja a sua sequencia de Collatz. "))

while num != 1:
    if num % 2 == 0:
        num = num / 2
        print(f"{num:.0f}")
    else:
        num = (3 * num) + 1
        print(f"{num:.0f}")


#Desafio 05: Desenvolva um jogo de adivinhação onde o programa escolhe um número aleatório entre 1 e 100. O usuário deve tentar adivinhar o número, e o programa deve fornecer dicas 
# se o palpite está muito alto ou baixo.

from random import randint

num_aleatorio = randint(1 , 101)
num_usuario = 0

while num_usuario != num_aleatorio:
    if num_usuario > num_aleatorio:
        print("O número digitado está alto.")
    else:
        print("O número digitado está baixo.")
    num_usuario = int(input("Tente adivinhar o número misterioso que está entre 1 e 100."))
print(f"parabéns, você acertou! O número misterioso era {num_aleatorio}")
    