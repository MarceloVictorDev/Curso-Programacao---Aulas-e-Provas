#[PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

def media(a, b, c):
    media_arit = (a + b + c) / 3
    return media_arit

print("-" * 45)
print("Bem vindo ao Calculo de média aritmética.")
print("-" * 45)

num1 = float(input("Digite aqui o primeiro número: "))
num2 = float(input("Digite aqui o segundo número: "))
num3 = float(input("Digite aqui o último número: "))

print(f"A média Aritmética dos números inseridos foi: {media(num1, num2, num3):.2f}")