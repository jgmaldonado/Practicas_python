#https://parzibyte.me/blog/2021/07/24/python-ejercicio-casino-ruleta-tragamonedas/#more-14550
# ingresar apuesta minimo 5000 pesos (validar)
# Ingresar un numero entre 1 -100, color negro o rojo y si es par e impar.
#Si se aciertan número la apuesta se multiplica por 10.
#Si se aciertan número y color, la apuesta se multiplica por 12.
#si se acierta solo el color, la apuesta se multiplica por 2
#Si se acierta entre las opciones de número par o impar, sólo no se pierde la apuesta.
#en cualquier otro caso pierde la apuesta
#generar numero aleatorio (ramdon.randint)
import random
ruleta=True
premio=i=0
while ruleta==True:
    i=i+1
    #cantidad = int(input("Dígame una cantidad en pesetas: "))
    if i==1:
        apuesta = int(input("dinero a apostar"))
    
    nro=int(input("Ingresar un numero entre 1 - 36"))
    color=int(input("1 rojo 2 negro"))
    poi=int(input("1 impar 2 par"))
    numero_aleatorio=random.randint(1,36)
    color2=random.randint(1,2)
    #color=random.choice["Rojo","Negro"]
    #print(random.choice(color))

    if nro==numero_aleatorio:
        premio=apuesta*10

    if color==color2:
        premio=apuesta*2

    if nro==numero_aleatorio and color==color2:
        premio=apuesta*12

    if numero_aleatorio % 2 == 0:
        print("El número sorteado es par")
        parImpar=2
    else:
        print("El número sorteado es impar")
        parImpar=1

    if parImpar==poi:
        if premio!=0:
            print("Ha ganado "+str(premio))
        else:
            premio=apuesta 
            print("mantien su apuesta "+str(premio))
    else:
        premio=0

    print("Ud aposto "+str(apuesta), "y ha ganado "+str(premio))

    print("quiere seguir apostando 1 Si  2 No")
    ap=int(input())
    if ap==1:
        print("dobla apuesta(1) o disminuye (0)")
        dobdis=int(input())
        if dobdis==1:
            apuesta=apuesta*2
        else:
            apuesta=apuesta/2
    else:
        ruleta=False



    






# preguntar si quiere seguir apostando si es asi preguntar si dobla la apuesta o la disminuye 
# se debe calcular el nuevo monto