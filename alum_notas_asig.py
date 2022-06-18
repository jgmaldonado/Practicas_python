"""Haz un programa en Python que pida datos del alumnado y muestre estadísticas de cada cual y estadísticas de la clase en general. 
Pedir datos de alumnos de una asignatura. 
Pedir nombre, edad, asignatura, si es por primer, segunda o tercer vez. y las 3 notas obtenidas en las evaluaciónes.
Se preguntará si van a introducirse los datos de más alumnos. 
En caso afirmativo, se repetirán los pasos anteriores hasta que se conteste que no. 

Mostrar estadísticas de la clase (cuando ya no haya más alumnos).
- 
- obtener promedio de notas de la asignatura, la nota max y la nota minima del curso.
- cantidad de alumnos del curso
- cantidad de notas aprobadas y reprobadas
- la nota media de los reprobados.
- la edad promedio del curso
- la cantidad de alumnos que toman asignatura por primera vez. 
- la cantidad de alumnos reprobados que estan en el curso por segunda o tercer vez
De los alumnos:
- el promedio de notas para cada alumno con su nombre y mostrar si la asignatura está aprobada o reprobada.
- indicar que si el promedio es inferior a 5 y superior a 2,7 debe dar examen.
- alumno con la nota mas alta. """


ac=may=j=ap=rp=ed=primera=seg=0
men=7
for i in range(4):
    n=str(input("diga su nombre"))
    edad = int(input()); asig=input()
    nota1=float(input())
    nota2=float(input());nota3=float(input())
    print("Asignatuta por 1 2 o 3 vez")
    opor = int(input())
    prom=(nota1+nota2+nota3)/3
    ac=ac+prom     #acumular para sacar promedio de todos dividir por n 
    promTodos=ac/4
    if prom>may:    #buscar mayor
        may=prom
        mateo=n     # alumno no mas alta
    if prom<men:     #buscar menor
        men=prom
    j=j+1      # cantidad alumnos contador 
    if prom>=4:     #contar notas aproba
        ap=ap+j
    else:
        rp=rp+j    #contar notas reprob.
    
    ed=ed+edad   # acumular edad y sacar promedios edades
    promEd=ed/j   

    if opor==1:            #alumnos que toman curso por 1 vez
        primera=primera+1
    
    if prom<4:             #reprobados que toman el curso por 3 o 4 
        if opor==2 or opor==3:
            seg=seg+1
        
    if prom>4:       # promedio cada alumno y nombre y si esta aprob o reprob
        print("promedio es",prom, "de ",n, "Aprobado ")
    else:
        print("promedio es",prom, "de ",n, "Reprobado ")

    if prom<5 and prom>2.6:    # si da examen 
        print("Debe rendir examen ")
    else:
        print("No da examen ")

    print("desea ingresar mas datos? presione 1 para continuar 0 para salir")  # preguntar si quiere seguir ingresando. 

    res=int(input())
    if res==0:
        break

print("Obtener promedio de notas de la asignatura  ", promTodos)
print("Promedio mas alto  ", may)
print("Promedio mas bajo  ", men)
print("Cantidad alumnos   ", j)
print(f"Notas aprobadas {ap} reprobadas {rp}  ")
print("Promedio edades  ", promEd)
print("Promedio mas bajo  ", men)
print(f" primera oportunidad {primera} reprobados en 2 y 3 {seg}  ")
print(f"Alumno nota mas alta {mateo} promedio {may}  ")




