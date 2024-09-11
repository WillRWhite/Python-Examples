# import turtle

# t1 = turtle.Turtle()
# t1.color("red") 
# t1.forward(80)

# turtle.done()

###############################################

# import turtle as tut

# t1 = tut.Turtle()
# t1.color("blue") 
# t1.forward(80)
# tut.done()

###############################################

# import turtle as tut

# t1 = tut.Turtle()
# t1.color("blue") 
# t1.forward(80)
# tut.done()

###############################################

from turtle import Turtle, done

pen = Turtle()

pen.color("green") 
pen.hideturtle()
pen.speed(10)

for _ in range(4):
    pen.forward(80)
    pen.right(90)
done()

###############################################

