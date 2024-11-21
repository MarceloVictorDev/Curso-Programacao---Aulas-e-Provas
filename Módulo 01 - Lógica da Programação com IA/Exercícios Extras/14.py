# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.

# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa 
# de R$ 4,00 por quilo excedente.

# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.

# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input('Por favor, digite o peso da pesca: '))

if peso_peixe > 50:
    peso_multa = peso_peixe - 50
    multa = peso_multa * 4
    print(f"Você excedeu o peso em {peso_multa:.2f} Kgs. Sua multa é de {multa:.2f} reais.")
else:
    print(f"Você pescou {peso_peixe} kgs.")

