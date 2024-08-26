import turtle
bob= turtle.Turtle()
bob.color("red","yellow")
# bob.background("rgb(255,255,255")
bob.speed(1)
bob.begin_fill()
for i in range(36):
    bob.forward(200)
    bob.left(170)
bob.end_fill()
turtle.done()