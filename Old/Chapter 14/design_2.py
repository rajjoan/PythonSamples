import turtle
colors = ["red","orange","yellow","green","blue","purple"]

turtle.bgcolor("black")
t=turtle.Pen()
t.speed(100)
t.shape("turtle")
for i in range(500):
    t.pencolor(colors[i%6])
    t.width(i/100+1)
    t.forward(100+i)
    t.right(90+i)
