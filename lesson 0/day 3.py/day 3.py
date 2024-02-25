from turtle import *

# houses

speed(100000)
width(5)

color("purple")

forward(100)
left(90)
forward(100)
left(90)
forward(100)
right(132)
forward(76)
right(96)
forward(75)
right(132)
forward(100)
left(90)
forward(101)

# painting door

left(91)
forward(35)

color("blue")

left(89)
forward(40)
right(90)
forward(30)
right(90)
forward(40)

# end door

# painting windows

penup()
goto(70,70)
pendown()

color("yellow")

forward(15)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)
penup()
goto(30,70)
pendown()

forward(15)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)
# second house
penup()
goto(125, 0)
pendown()

color("green")

forward(100)
right(45)
forward(75)
right(90)
forward(75)
right(50)
right(85)
forward(105)
backward(105)
left(90)
forward(100)
right(90)
forward(105)
right(180)
forward(40)

color("pink")

left(90)
forward(40)
right(90)
forward(25)
right(90)
forward(40)

# painting windows

penup()
goto(200,70)
pendown()

color("brown")

forward(15)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)

penup()
goto(150,70)
pendown()

forward(15)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)

# end second house

# painting third house

penup()
goto(0,-200)
pendown()

color("gray")

forward(100)
right(45)
forward(75)
right(90)
forward(75)
right(135)
forward(105)
backward(105)
left(90)
forward(100)
right(90)
forward(105)
right(180)
forward(40)

color("purple")

left(90)
forward(40)
right(90)
forward(25)
right(90)
forward(40)

# painting windows for third house

penup()
goto(15,-135)
pendown()

color("blue")

forward(15)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)

penup()
goto(95,-135)
pendown()

forward(15)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)

# fourth house

penup()
goto(125,-200)
pendown()

color("purple")

forward(100)
right(45)
forward(75)
right(90)
forward(75)
right(135)
forward(105)
backward(105)
left(90)
forward(100)
right(90)
forward(105)
left(180)
forward(40)

color("yellow")

left(90)
forward(40)
right(90)
forward(25)
right(90)
forward(40)

# windows for forth house

penup()
goto(200,-130)
pendown()

color("orange")

forward(15)
left(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)

penup()
goto(140,-130)
pendown()

backward(15)
left(90)
forward(15)
right(90)
forward(15)
right(90)
forward(15)

# end houses

penup()
goto(125,-200)
pendown()

color("light green")

right(90)
forward(1000)
left(180)
forward(2000)

penup()
goto(-300,-200)
pendown()

color("brown")

right(90)
forward(200)
right(90)
forward(30)
right(90)
forward(15)
right(180)
right(90)

color("green")

circle(65)

color("brown")

left(90)
forward(15)
right(90)
forward(30)
right(90)
forward(200)

penup()
goto(300,300)
pendown()

color("yellow")

circle(65)

penup()
goto(115,-390)
pendown()

color("light green")

left(90)

circle(195)

penup()
goto(0,0)
pendown()

color("black")

right(90)
forward(35)

penup()
goto(230,0)
pendown()

forward(35)

exitonclick()