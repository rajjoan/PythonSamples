
import turtle
turtle.bgcolor("Black")
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
for i in range(1,1000,5):
    t.pencolor("DeepPink")
    t.forward(50+i)
    t.pencolor("Cyan")
    t.right(144)

turtle.done()
