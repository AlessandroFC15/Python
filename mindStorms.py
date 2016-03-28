import turtle

def drawSquare(initialAngulation):
    drawer = getDefaultDrawer()

    drawer.right(initialAngulation)

    for i in range(0,4):
        drawer.forward(100)
        drawer.right(90)

def drawCircle():
    drawer = getDefaultDrawer()
    
    drawer.circle(100)

def drawTriangle():
    drawer = getDefaultDrawer()

    for i in range(0,3):
        drawer.forward(100)
        drawer.left(120)
        drawer.forward(100)
        drawer.left(120)
        drawer.forward(100)
        drawer.left(120)

def addScreen():
    window = turtle.Screen()
    window.bgcolor("black")
    return window

def getDefaultDrawer():
    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.hideturtle()
    drawer.color("white")

    return drawer

def drawCircle(angulation):
    drawer = getDefaultDrawer()

    drawer.right(angulation)

    drawer.circle(100)

screen = addScreen()

for i in range(0, 20):
    drawCircle(i * 18)
    

screen.exitonclick()
