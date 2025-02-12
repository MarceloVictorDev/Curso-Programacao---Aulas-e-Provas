#1[PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.
import random

def lancar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(f"O dado 1 saiu: {dado1}\n")
    print(f"O dado 2 saiu: {dado2}\n")
    print(f"A soma dos dados foi: {dado1+dado2}")
    return 

lancar_dados()