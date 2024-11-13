import turtle
t=turtle.Turtle()

side=int(input("Enter a number of sides  : "))
length=int(input("Enter a length  : "))
angle=360.0/side

for i in range(side):
    t.forward(length)
    t.right(angle)

    
  
    
