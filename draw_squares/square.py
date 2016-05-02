import turtle
import time

def draw_square(brad):
    for n in range(0,72):
        for i in range(0,4):
            if (i % 2 != 0):
                brad.forward(100)
                brad.right(30)
            elif (i == 2):
                brad.forward(100)
                brad.right(150)
            else:
                brad.forward(100)


        brad.right(5)

def return_square(turtle):
    turtle.goto(0.0,0.0)

def stem(a):
    a.right(90)
    a.forward(400)
# def draw_circle(veronica):
#     veronica.circle(75)
#
# def draw_triangle(kevin):
#     # kevin.right(150)
#     kevin.right(180)
#     kevin.forward(120)
#     kevin.left(90)
#     kevin.forward(90)
#     kevin.left(130)
#     kevin.goto(0.00,0.00)
#     kevin.right(30)

window = turtle.Screen()
window.bgcolor("orange")
# window.color("blue")
window.title("Turtle Drawing Squares")

a = turtle.Turtle()
a.color("blue")
a.speed(20)
a.shape("circle")

draw_square(a)
return_square(a)
stem(a)


window.exitonclick()
