import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for i in range(360):
    t.color(colors[i % 6])
    t.forward(i * 3 / 2 + i)
    t.left(59)

turtle.done()
