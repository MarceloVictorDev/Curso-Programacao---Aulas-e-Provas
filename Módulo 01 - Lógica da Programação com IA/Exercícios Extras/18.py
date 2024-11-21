# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
# aproximado de download do arquivo usando este link (em minutos).


tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB."))
velocidade_internet = float(input("Digite a velocidade de internet, em Mbps."))

tempo = (tamanho_arquivo * 8) / velocidade_internet
minutos = tempo // 60
segundo = tempo % 60
print(f"O tempo de download será de: {minutos:.2f} minutos e {segundo:.2f} segundos.")
