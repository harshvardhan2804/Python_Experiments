import turtle

# object tr for turtle
tr = turtle.Turtle()


sz = int(turtle.textinput("Enter radius of circle :","radius"))

# set thickness for each ring
tr.pensize(5)

tr.color("blue")
tr.penup()
tr.goto(-110, -25)
tr.pendown()
tr.circle(sz)

tr.color("black")
tr.penup()
tr.goto(0, -25)
tr.pendown()
tr.circle(sz)

tr.color("red")
tr.penup()
tr.goto(110, -25)
tr.pendown()
tr.circle(sz)

tr.color("yellow")
tr.penup()
tr.goto(-55, -75)
tr.pendown()
tr.circle(sz)

tr.color("green")
tr.penup()
tr.goto(55, -75)
tr.pendown()
tr.circle(sz)
