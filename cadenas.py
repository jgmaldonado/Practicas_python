
cadena="Juan Guillermo Maldonado Rojas  "
for i in cadena:
    print(len(cadena))
    print(cadena.upper())   
    print(cadena.lower())
    print(cadena.strip())
    x = cadena.rfind(" ")
    print(x)
    pate=cadena[0:2:1]
    print(pate)
    print(cadena[0:2:1])
    #cadena[inicio:final:saltos]

#frase = input("Introduce una frase: ")
print(cadena[::-1])
"""
###### interes
mount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? ")) #10
years = int(input("¿Años?"))
for i in range(years):
    #mount*= 1 + interest / 100 
    mount= mount * (1 + interest / 100) 
    print("Capital tras " + str(i+1) + " años: " + str(round(mount, 2)))

####


def imc_cal(peso,talla):
    imc= peso/talla**2
    print (imc)
    if imc>30: 
        print ("Obeso ")
    elif imc>25:
        print ("tiene sobrepeso")
    elif imc>19:
        print ("Peso normal")
    else: 
        print ("Esta desnutrido")
    
    return(imc)

print("como esta su imc")
imc=valor=(float)
x=int(input("ingrese su peso en kg"))
y=float(input("ingrese su talla en mt"))

calc=imc_cal(x,y)
print(f"Su imc es: {calc} ud. esta")

"""

