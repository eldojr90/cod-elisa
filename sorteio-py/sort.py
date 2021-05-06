from random import randint


lista = [
		'Elisa', #1		#0
		'Eldo Jr', #2		#1
		'Eliana', #3		#2
		'Bolo Boy', #4	#3
		'Joyce', #5		#4
		'Aline', #6		#5
		'Thaís', #7		#6
		'Cynthia', #8		#7
		'Thaísa',		#8
		'Matheus',		#9
		'Marcus',		#10
		'Palmira',		#11
		'Eldo',		#12 ou 13
	]
	
tamanho_da_lista = len(lista) #13
numero_sorteado = randint(1, tamanho_da_lista) # de 1 a 13
indice = numero_sorteado - 1 # < 13

vencedor = lista[indice]
	
print( vencedor )
