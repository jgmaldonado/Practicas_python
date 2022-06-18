
## Mostrar Nombre y promedio mejor alumno y nombre promedio mas bajo
#print("Promedios 10 alumnos")   
"""
mayor_nota=0
mpro=str()
menor_nota=0
mepro=str()


for i in range(1,4):
    nota=float(input("Ingrese su promedio "+" "))
    nombre=input("Ingrese su Nombre ")
    if nota>mayor_nota:
        mayor_nota=nota
        mpro=nombre
    if i == 1:
        menor_nota=nota
    if nota<menor_nota:
        menor_nota=nota
        mepro=nombre
print("ALUMNO   : ",mpro)
print("PROMEDIO MAYOR: ",mayor_nota)
print("ALUMNO   : ",mepro)
print("PROMEDIO MENOR: ",menor_nota)

    

## USO BREAK CUANDO PILLA UN 0
cuenta = "2356578420254223"
cuenta2=str(42197365097134)

for x in cuenta:
  print(x)
  if x == "0":
    break

for i in cuenta2:
    print(i)
    if i==3:
        break 

############ CICLO MIENTRAS 
i = 1
while i < 6:
  print(i)
  i += 1
  #i=i+1

########print("adivinar el numero entre 1 y 20")
import random
numero=random.randint(1,20)
i = 1
intento=j=0
while i != 0:
    print("Adivine el numero. Tiene 6 intentos, si se rinde presione 0 ")
    nro=int(input("Ingrese nro"))
    j=j+1
    if nro==numero:
        print("Felicitaciones adivinaste!!")
        break
    else:
        if j==6:
            break
    print("intento "+str(j))

#### Random dados
import random

total = 0
for i in range(1,4):
    dado = random.randrange(1, 6)
    #print(f"Tirada {i}: {dado}")
    print("Tirada: ",dado)
    total += dado
print(f"En total ha obtenido {total} punto(s).") 

####### Estacionamiento 
print("Ingresa el valor de horas:")
horas = float(input())
print("Ingresa el valor de minutos:")
minutos = float(input())
print("Selecciona el valor de tipo de vehiculo.")
print("    1.- Automóvil")
print("    2.- Camioneta")
print("    3.- Motocicleta")
tipo_de_vehiculo = input()
if tipo_de_vehiculo==1:
	costo_por_hora = 600
if tipo_de_vehiculo==2:
	costo_por_hora = 800
if tipo_de_vehiculo==3:
	costo_por_hora = 300
pago = horas*costo_por_hora   # costo por horas
if minutos<20:
	costom = 300
elif minutos<40:
    costom= 600
else:
	costom = 900
print("Valor por hora: ",pago)
print("Valor por minutos: ",costom)
print("Total a pagar ",pago+costom) 

#masculino = 0 
"""
"""
i = ac=j=hombre=mujer=h1=m1=0
count = 0
while i<4:
	print("ingrese sexo")
	print("h hombre o m mujer")
	sexo = input()
	print("ingrese edad")
	edad = int(input())
	i = i+1
	if edad>18:
		ac = ac+edad   # acumula edad
		j = j+1    # cuantos son >18

	if sexo=="h":
		hombre = hombre+1   #cuantos son    
		count = count+1     # inutil 
		if edad>h1:       #buscar el mayor
			h1 = edad
	elif sexo=="m":
		mujer = mujer+1    # cuantas son
		count = count+1      #inutil 
		if edad>m1:
			m1 = edad      #guarda el mayor
# calculos
prom = ac/j     #promedio edad mayores de edad 
porceh = (hombre/4)*100    
porcem = (mujer/4)*100 
# salidas
print("la cantidad de hombres es: ",hombre)
print("la cantidad de mujeres es: ",mujer)
print("el porcentaje de hombres es: ",porceh)
print("el porcentaje de mujeres es: ",porcem)
print("la edad mas alta en hombres es: ",h1)
print("la edad mas alta en mujeres es: ",m1)
print("el promedio es: ",prom)      """

#print("Ingrese cantidad de encuestados")
n=int(input("Ingrese cantidad de encuestados"))
rock1=menores=admay=menosPop=0
for i in range(n):

    print("Ingrese su edad")
    edad=int(input())
    print("Ingrese su categoria favorita")
    print("Opción 1 : Rock")
    print("Opción 2 : Pop")
    print("Opción 3 : Folclore")
    print("Opción 4 : Jazz")
    op=int(input())
    
    if edad>18 and op==1:
        rock1+=1
    porc1=rock1/n*100   # % aduktos gusta rock
    
    if edad<18 and op==3:
        menores=menores+1

    if edad>65:
        if op==2 or op==4:
            admay=admay+1
    
    if edad>18:
        if op==1 or op==3 or op==4:
            menosPop=menosPop+1
    porc2=menosPop/n+100
    
print("Total de adultos (incluye mayores) el rock: ",rock1)
print("Porcentaje de adultos (incluye mayores) que les gusta el rock: ",porc1)
print("Menores que les gusta el folclore: ",menores)
print("Adultos mayores que les gusta el pop o jazz: ",admay)
print("Porcentaje de adultos que les gusta todo menos el pop", porc2)