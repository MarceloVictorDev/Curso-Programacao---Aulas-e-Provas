#[PYIA-A01] Crie uma lista contendo seis frutas de sua escolha. Depois de ter a lista pronta, converta essa lista em uma tupla. Por fim, exiba o conteúdo da tupla resultante para verificar as frutas que foram armazenadas.

#Criando a lista com 06 Frutas
frutas = ["Morango", "Uva", "Maça", "Pera", "Melancia", "Limão"]

#Convertendo a lista de frutas em uma tupla.
frutas_tuplas = tuple(frutas)

#Imprimindo a tupla de frutas.
print(f"A frutas armazenadas são: {frutas_tuplas} e é do tipo: {type(frutas_tuplas)}.")