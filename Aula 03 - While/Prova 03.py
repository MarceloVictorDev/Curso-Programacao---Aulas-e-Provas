#Nessa prova estarei utilizando num_total_tentativas como sendo 04, para que consiga exibir o número de tentativas corretas para o usuário iniciando como 01, e não como 00. 
# Importante frisar que a variável "tentativas" está iniciando como 01. 
# Ou seja: (num_total_tentativas - tentativas) = 03 tentativas totais para o usuário.

num_adivinhar = 7
num_chute = 0
tentativas = 1
num_total_tentativas = 4

print("Você terá três tentativas para tentar acertar o número misterioso.")

while tentativas <= 4:
    num_chute = int(input(f"Tentativa {tentativas}. Digite um número: "))
    if num_chute == num_adivinhar: 
        print("Parabéns, você acertou o número misterioso.")
        break
    elif num_chute != num_adivinhar: 
        tentativas += 1
        print(f"Número errado. Você ainda tem {num_total_tentativas - tentativas} tentativas.")
    if tentativas == 4:
        print(f"Não foi dessa vez, mas não fique triste. Você poderá tentar novamente.")
        break


