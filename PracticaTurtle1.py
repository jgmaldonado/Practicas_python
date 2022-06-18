import turtle
import random

av=random.randint(10,200)
wn = turtle.Screen()
wn.title("Tortugas")
wn.bgcolor("lightgreen")

turtle.shape()
turtle.color('red')
turtle.pensize(4)
turtle.pencolor("blue")

for i in range(50):
    turtle.left(10)
    turtle.forward(av)

turtle.penup()
turtle.forward(150)
turtle.pendown()
'''valor=int(input("ingrese cantidad de repeteciones"))
avance=int(input())
i=0
while i<valor:
     turtle.left(6)
     turtle.forward(avance)
     i+=1
'''
   
wn.exitonclick()
