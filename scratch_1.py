import turtle


screen = turtle.Screen()
screen.setup(500,700)
screen.bgcolor('lightblue')
t=turtle.Turtle()
t.speed(300)



#snow on the ground
t.penup()
t.goto(-250,-200)
t.pensize(20)
t.pencolor('white')
t.fillcolor('white')
t.pendown()
t.begin_fill()
t.forward(500)
t.right(90)
t.forward(250)
t.right(90)
t.forward(500)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.end_fill()
t.goto(-250,-201)
t.fillcolor('white')
t.speed(10)
t.penup()
t.goto(-250,-190)
t.pendown()
t.setheading(0)
t.pensize(2)
t.pencolor('black')
t.forward(500)
t.penup()


#snowman base
t.penup()
t.goto(-175,-202)
t.pencolor('white')
t.fillcolor('white')
t.pendown()
t.begin_fill()
t.circle(50)
t.penup()
t.goto(-175,-110)
t.pendown()
t.circle(40)
t.penup()
t.goto(-175,-35)
t.circle(30)
t.penup()
t.pendown()
t.end_fill()
t.penup()



#snowman face
t.left(90)
t.forward(30)
t.pencolor('black')
t.fillcolor('orange')
t.begin_fill()
t.right(90)
t.right(15)
t.pendown()
t.forward(30)
t.pencolor('black')
t.fillcolor('orange')
t.goto(-175,-15)
t.goto(-175,-13)
t.goto(-175,-5)
t.end_fill()
t.penup()
t.goto(-184,1)
t.pendown()
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.circle(4)
t.end_fill()
t.penup()
t.goto(-163,1)
t.pendown()
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.circle(4)
t.end_fill()
t.penup()


#buttons
t.goto(-184,-21)
t.pendown()
t.goto(-157,-21)
t.penup()
t.goto(-175,-55)
t.pendown()
t.begin_fill()
t.circle(4)
t.end_fill()
t.penup()

t.goto(-175,-75)
t.pendown()
t.begin_fill()
t.circle(4)
t.end_fill()
t.penup()

t.goto(-175,-90)
t.pendown()
t.begin_fill()
t.circle(4)
t.end_fill()
t.penup()

t.goto(-140,-58)
t.pendown()
t.pensize(4)
t.pencolor('SaddleBrown')
t.goto(-100,-90)
t.penup()
t.goto(-210,-62)
t.setheading(235)
t.pendown()
t.forward(50)
t.penup()


candy = turtle.Turtle()
candy.pensize(5)
candy.color("red")

candy.penup()
candy.goto(100,-200)
candy.pendown()
candy.setheading(90)
candy.forward(50)
candy.right(90)
candy.forward(10)
candy.right(90)
candy.forward(10)
candy.penup()
candy.goto(140, -200)
candy.pendown()
candy.setheading(90)
candy.forward(50)
candy.right(90)
candy.forward(10)
candy.right(90)
candy.forward(10)
candy.penup()

#cloud code
cloud = turtle.Turtle()
cloud.pensize(5)
cloud.color("white")


sky = turtle.Turtle()
sky.pensize(5)
sky.color("yellow")

sky.penup()
sky.goto(-180,250)
sky.pencolor('yellow')
sky.fillcolor('yellow')
sky.pendown()
sky.begin_fill()
sky.circle(35)
sky.end_fill()








cloud.penup()
cloud.goto(-200,250)
cloud.pencolor('white')
cloud.fillcolor('white')
cloud.pendown()
cloud.begin_fill()
cloud.circle(20)
cloud.forward(35)
cloud.circle(20)
cloud.forward(2)
cloud.circle(20)
cloud.forward(33)
cloud.circle(20)
cloud.forward(20)
cloud.circle(20)
cloud.penup()
cloud.end_fill()








tree = turtle.Turtle()
tree.pensize(5)
tree.color("saddlebrown")
tree.pensize(20)

tree.penup()
tree.goto(-5,-200)
tree.pendown()
tree.left(90)
tree.forward(80)


tree.goto(-5,-130)

tree.pensize(7)
tree.fillcolor('green')
tree.pendown()
tree.begin_fill()
tree.color("green")
tree.right(120)
tree.forward(55)
tree.goto(-1,110)
tree.goto(-5,-130)
tree.end_fill()
tree.fillcolor('green')
tree.pendown()
tree.begin_fill()
tree.color("green")
tree.right(120)
tree.forward(55)
tree.goto(-1,110)
tree.goto(-1,-115)
tree.end_fill()
tree.penup()


tree.goto(-5,-200)









t.speed(0)
t.penup()
t.goto(-100,-200)
t.pendown()
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.goto(-100,-130)
t.setheading(0)
t.pencolor("red")
t.forward(70)
t.pencolor("red")
t.goto(-30,-200)
t.goto(-100,-200)
t.end_fill()

t.penup()
t.pencolor('black')
t.fillcolor('black')
t.pensize(10)
t.goto(-100,-130)
t.pendown()
t.forward(70)
t.penup()
t.pencolor('yellow')
t.fillcolor('red')
t.goto(0,100)
t.pendown()
t.circle(10)
t.penup()
t.goto(2,-100)
t.pencolor('red')
t.fillcolor('red')
t.pendown()
t.circle(4)
t.penup()
t.goto(2,-50)
t.pencolor('blue')
t.fillcolor('blue')
t.pendown()
t.circle(4)




candy.hideturtle()
cloud.hideturtle()
sky.hideturtle()
tree.hideturtle()

candy.speed(300)
cloud.speed(300)
sky.speed(300)
tree.speed(300)


turtle.done()