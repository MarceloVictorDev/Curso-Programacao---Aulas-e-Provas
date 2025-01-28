#[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.

def maior_numero(a, b, c):
    
    if a >= b and a >= c:
        maior = a
    elif b >= a and b >= c:
        maior = b
    elif c >= a and c >= b:
        maior = c
    return maior

num1 = int(input("Digite aqui o primeiro número: "))
num2= int(input("Digite aqui o segundo número: "))
num3 = int(input("Digite aqui o último número: "))

print(f"O maior número digitado foi: {maior_numero(num1, num2, num3)}")
