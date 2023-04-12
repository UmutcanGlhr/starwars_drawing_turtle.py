import turtle

def starwars():
    s = turtle.Screen()
    s.setup(width = 0.7, height = 0.8)
    s.bgpic('Vader.png')
    t = turtle.Turtle()
    

    def curve(value):
        for i in range(value):
            t.forward(1)
            t.right(1)

    def curve1(value):
        for i in range(value):
            t.forward(0.5)
            t.left(1)
    def curve11(value):
        for i in range(value):
            t.forward(2)
            t.left(1)   
            

    t.speed(11)
    t.width(12)
    t.pensize(7)
    t.penup()
    t.setposition(-350,110)
    t.pendown()
    t.pencolor("yellow")
    

    t.forward(100)

    curve1(140)
    t.forward(30)

    t.right(140)
    t.forward(60)
    t.right(90)

    t.forward(80)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(80)

    t.right(90)
    t.forward(60)

    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(170)
    curve1(140)
    t.forward(30)
    t.right(140)
    t.forward(80)
    t.left(90)
    t.forward(30)




    t.penup()
    t.setposition(-115,90)
    t.pendown()
    t.left(90)

    t.forward(50)
    t.left(75)
    t.forward(20)
    t.right(75)
    t.forward(40)
    t.right(75)
    t.forward(20)
    t.left(75)
    t.forward(50)
    t.left(90)
    t.left(20)
    t.forward(130)
    t.left(70)
    t.forward(60)
    t.left(70)
    t.forward(130)

    t.left(20)
    t.left(90)

    t.penup()
    t.setposition(-60,145)
    t.pendown()
    t.forward(40)


    t.left(90)
    t.left(20)
    t.forward(50)
    t.left(70)
    t.left(65)
    t.forward(50)

    t.right(65)
    t.right(180)

    t.penup()
    t.setposition(55,90)
    t.pendown()

    t.forward(50)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.right(45)
    t.forward(70)
    curve1(40)
    t.left(5)
    t.forward(90)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(80)
    t.right(35)
    curve(20)
    t.right(35)
    t.right(90)
    t.circle(30,180)
    t.forward(113)
    t.left(90)
    t.forward(124)

    t.penup()
    t.setposition(105,170)
    t.pendown()
    t.left(90)
    t.forward(40)
    t.circle(10,180)
    t.forward(40)
    t.left(90)
    t.forward(20)

    t.left(90)
    t.penup()
    t.setposition(-370,80)
    t.pendown()
    t.forward(40)
    t.right(65)
    t.forward(60)
    t.right(25)
    t.left(90)
    t.left(65)
    t.forward(60)
    t.left(25)
    t.right(90)
    t.forward(40)

    t.right(65)
    t.forward(60)
    t.right(25)
    t.left(90)
    t.left(65)
    t.forward(60)

    t.left(25)
    t.right(90)
    t.forward(40)

    t.right(90)
    t.right(15)
    t.forward(130)
    t.left(15)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.left(15)
    t.forward(70)
    t.left(150)

    t.forward(70)
    t.left(15)
    t.right(90)
    t.forward(60)
    t.right(75)
    t.forward(130)
    t.right(15)
    t.right(90)

    def a (x,y):
        t.penup()
        t.setposition(x,y)
        t.pendown()
    
        

        t.forward(50)
        t.left(75)
        t.forward(20)
        t.right(75)
        t.forward(40)
        t.right(75)
        t.forward(20)
        t.left(75)
        t.forward(50)
        t.left(90)
        t.left(20)
        t.forward(130)
        t.left(70)
        t.forward(60)
        t.left(70)
        t.forward(130)

        t.left(20)
        t.left(90)

        t.penup()
        t.setposition(x+55,y+55)
        t.pendown()
        t.forward(40)


        t.left(90)
        t.left(20)
        t.forward(50)
        t.left(70)
        t.left(65)
        t.forward(50)

        

    a(-150,-50)


    t.penup()
    t.setposition(20,-50)
    t.pendown()
    t.right(65)
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.right(45)
    t.forward(70)
    curve1(40)
    t.left(5)
    t.forward(150)
    curve1(120)
    t.forward(50)
    t.right(120)
    t.forward(80)

    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(100)
    curve1(120)
    t.forward(50)
    t.right(120)
    t.forward(110)
    t.right(35)
    curve(20)
    t.right(35)
    t.right(90)
    t.circle(33,180)

    t.forward(125)
    t.left(90)
    t.forward(120)

    t.penup()
    t.setposition(70,20)
    t.pendown()
    t.left(90)
    t.forward(40)
    t.circle(10,180)
    t.forward(40)
    t.left(90)
    t.forward(20)

    t.hideturtle()
    turtle.done()
    
starwars()