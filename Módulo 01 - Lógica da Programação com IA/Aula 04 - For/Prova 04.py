##[LPIA-A04] Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao 
# usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
#Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares 
# no intervalo, caso seja o caso.
#Ao final, exiba a soma dos números pares encontrados.

num_inicio = int(input("Insira um número inteiro: "))
num_fim = int(input("Insira outro número inteiro: "))
soma_pares = 0

for numeros_intervalo in range(num_inicio, num_fim+1):
   if numeros_intervalo % 2 == 0:
      soma_pares += numeros_intervalo
else: 
    if soma_pares == 0:
        print(f"Não há números pares no intervalo entre {num_inicio} e {num_fim}.")
    else:
        print(f"A soma dos números pares no intervalo entre {num_inicio} e {num_fim} é: {soma_pares}.")


