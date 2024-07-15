import turtle
turtle.delay(10)
turtle.pensize(15)
##########
#body

turtle.penup()
turtle.setposition(-200, -50)
turtle.setheading(0)
turtle.pendown()
turtle.setposition(200, -50)

turtle.setheading(90)
turtle.setposition(200,150)

turtle.setheading(180)
turtle.setposition(-200, 150)

turtle.setheading(170)
turtle.setposition(-200, -50)

##########
#neck
turtle.penup()
turtle.setposition(-50, 150)
turtle.setheading(0)
turtle.pendown()
turtle.setposition(-50, 200)

turtle.penup()
turtle.setposition(50, 150)
turtle.setheading(0)
turtle.pendown()
turtle.setposition(50,  200)

############
#head
turtle.penup()
turtle.setposition(-175, 200)
turtle.setheading(0)
turtle.pendown()
turtle.setposition(175,  200)

turtle.setheading(90)
turtle.setposition(175, 335)

turtle.setheading(90)
turtle.circle(50, 95)

turtle.setheading(180)
turtle.setposition(-125, 385)

turtle.setheading(180)
turtle.circle(50, 95)

turtle.setheading(270)
turtle.setposition(-175, 200)

############
#eyes

turtle.penup()
turtle.setposition(-35, 275)
turtle.setheading(90)
turtle.pendown()
turtle.circle(30, 180)

turtle.penup()
turtle.setposition(100, 275)
turtle.setheading(90)
turtle.pendown()
turtle.circle(30,  180)

#############
#left hand

turtle.penup()
turtle.setposition(-200, 100)
turtle.pendown()
turtle.setposition(-250, 100)

turtle.penup()
turtle.setposition(-250, 150)
turtle.pendown()
turtle.setposition(-300, 150)

turtle.setheading(180)
turtle.circle(30, 90)

turtle.setheading(270)
turtle.setposition(-330, -75)

turtle.setheading(0)
turtle.setposition(-250, -75)

turtle.setheading(90)
turtle.setposition(-250, 150)

turtle.penup()
turtle.setposition(-290, -75)
turtle.pendown()
turtle.setposition(-290, -110)

turtle.penup()
turtle.setposition(-260, -150)
turtle.pendown()
turtle.setheading(90)
turtle.circle(30, 180)

###############
#right hand
turtle.penup()
turtle.setposition(200,100)
turtle.pendown()
turtle.setposition(250, 100)

turtle.penup()
turtle.setposition(250,150)
turtle.pendown()
turtle.setposition(250, -75)

turtle.setheading(0)
turtle.setposition(330, -75)

turtle.setheading(90)
turtle.setposition(330, 120)

turtle.setheading(90)
turtle.circle(30, 90)

turtle.setheading(180)
turtle.setposition(250, 150)

turtle.penup()
turtle.setposition(290,-75)
turtle.pendown()
turtle.setposition(290, -110)

turtle.penup()
turtle.setposition(320, -150)
turtle.pendown()
turtle.setheading(90)
turtle.circle(30, 180)

###############
#legs

turtle.penup()
turtle.setposition(-135, -50)
turtle.pendown()
turtle.setposition(-135, -150)

turtle.penup()
turtle.setposition(135, -50)
turtle.pendown()
turtle.setposition(135, -150)

turtle.penup()
turtle.setposition(185, -150)
turtle.pendown()
turtle.setposition(-185, -150)

turtle.setheading(180)
turtle.circle(50, 180)

turtle.setheading(0)
turtle.setposition(185, -250)

turtle.setheading(0)
turtle.circle(50,180)

turtle.penup()
turtle.setposition(-135, -185)
turtle.pendown()
turtle.setposition(-135, -215)

turtle.penup()
turtle.setposition(-70, -185)
turtle.pendown()
turtle.setposition(-70, -215)

turtle.penup()
turtle.setposition(0, -185)
turtle.pendown()
turtle.setposition(0, -215)

turtle.penup()
turtle.setposition(70, -185)
turtle.pendown()
turtle.setposition(70, -215)

turtle.penup()
turtle.setposition(135, -185)
turtle.pendown()
turtle.setposition(135, -215)


