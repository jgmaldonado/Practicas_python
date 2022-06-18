
print("Ingresa el valor de n:")
n = float(input())
for i in range(1,n+1):
	print("Ingresa la edad:")
	edad = input()
	print("Selecciona .")
	print("    1.- Rock")
	print("    2.- Pop")
	print("    3.- Folclore")
	print("    4.- Jazz")
	mus = input()
	if edad>18:
		if mus==1:
			# cuantos adultos les gusta el rock
			j = j+1
			# porcentaje adultos gusta rock
			porc = j/n*100
	if edad<18:
		if mus==3:
			# cuantos menores les gusta el folclore
			k = k+1
	if edad>65:
		if mus==2 or mus==4:
			# cuantos adultos mayores  les gusta el pop y jazz
			l = l+1
	if edad>18 and edad<65:
		if mus!=2:
			# adultos les gusta todo menos pop
			m = m+1
			porc1 = m/n*100
print("cuantos adultos les gusta el rock ",j)
print("porcentaje adultos gusta rock ",porc)
print("cuantos menores les gusta el folclore ",k)
print("cuantos adultos mayores  les gusta el pop y jazz ",l)
print("% adultos les gusta todo menos pop ",porc1)

