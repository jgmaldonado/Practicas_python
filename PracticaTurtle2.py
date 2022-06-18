import turtle
import random

# configuramos la pantalla

turtle.setup(900, 800)
win = turtle.Screen()
win.bgcolor("lavender")
win.title("Juego tortugas")

# creamos  tortuga Maria

maria = turtle.Turtle()
maria.color("violet")
maria.pensize(3)
maria.shape("turtle")   
maria.speed(5)
maria. penup()         

# creamos tortuga Juan

juan = turtle.Turtle()
juan.color("blue")
juan.pensize(3)
juan.shape("turtle")
juan.speed(4)
juan. penup()

# posicion de partida

#maria.goto(10,-210)

#juan.goto(-10,-250)

maria.left(70)
juan.left(70)

#inicio carrera
maria.stamp()
juan.stamp()
maria.pendown()
juan.pendown()

for i in range(16):
    num1=random.randint(75, 100)
    num2=random.randint(75, 100)
    
    maria.forward(num1)
    juan.forward(num2)
    maria.left(25)
    juan.left(25)

maria.stamp()
juan.stamp()
win.exitonclick()