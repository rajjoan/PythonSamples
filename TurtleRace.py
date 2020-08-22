
import turtle
import random

turtle.bgcolor("Black")

p1=turtle.Turtle()
p1.color("Cyan")
p1.shape("turtle")
p1.penup()
p1.goto(-200,100)
p2=p1.clone()
p2.color("HotPink")
p2.penup()
p2.goto(-200,-100)

p1.goto(300,60)
p1.pendown()
p1.circle(40)
p1.penup()
p1.goto(-200,100)
p2.goto(300,-140)
p2.pendown()
p2.circle(40)
p2.penup()
p2.goto(-200,-100)

die=[1,2,3,4,5,6]
for i in range(20):
    if p1.pos()>=(300,100):
          print("Player One Wins!!!")
          break
    elif p2.pos()>=(300,-100):
        print("Player Two Wins!!!")
    else:
        p1_turn=input("Press 'Enter' to roll the die , Player 1")
        die_outcome=random.choice(die)
        print("The result of the die is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        p1.fd(20*die_outcome)
        p2_turn=input("Press 'Enter' to roll the die , Player 2")
        die_outcome=random.choice(die)
        print("The result of the die is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        p2.fd(20*die_outcome)
        

