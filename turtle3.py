import turtle
import math
bob= turtle.Turtle()
bob.color("red","yellow")
# bob.background("rgb(255,255,255")
bob.speed(10)
# bob.begin_fill()
for i in range(2000):
    bob.forward(math.sqrt(i))
    bob.left(i%100)


# bob.end_fill()
turtle.done()