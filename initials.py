import turtle

# Constants
LENGTH_ARESTA = 50

def drawInitials():
    screen = addScreen()
    
    drawer = getDefaultDrawer()

    setInitialPosition(drawer)

    drawE(drawer)

    drawA(drawer)

    drawF(drawer)

    drawC(drawer)

    screen.exitonclick()

def setInitialPosition(drawer):
    drawer.penup()
    drawer.setpos(-125, 0)
    drawer.pendown()

def drawC(drawer):
    drawer.forward(LENGTH_ARESTA)
    drawer.backward(LENGTH_ARESTA)

    drawer.left(90)
    drawer.forward(LENGTH_ARESTA * 2)

    drawer.right(90)
    drawer.forward(LENGTH_ARESTA)

    # Adjust position to next letter
    adjustDrawerPosition(drawer)

def drawA(drawer):
    drawer.left(90)
    drawer.forward(LENGTH_ARESTA * 2)

    drawer.right(90)
    drawer.forward(LENGTH_ARESTA)

    drawer.right(90)
    drawer.forward(LENGTH_ARESTA)

    drawer.right(90)
    drawer.forward(LENGTH_ARESTA)
    drawer.backward(LENGTH_ARESTA)

    drawer.left(90)
    drawer.forward(LENGTH_ARESTA)
    drawer.left(90)
    
    # Adjust position to next letter
    adjustDrawerPosition(drawer)
    
def drawE(drawer):
    # Drawing bottom line
    
    drawer.forward(LENGTH_ARESTA)
    drawer.backward(LENGTH_ARESTA)

    drawF(drawer)

def drawF(drawer):
    # Draw lower tronco

    drawer.left(90)
    drawer.forward(LENGTH_ARESTA)

    # Draw middle line
    drawer.right(90)
    drawer.forward(LENGTH_ARESTA/1.5)
    drawer.backward(LENGTH_ARESTA/1.5)

    # Draw upper tronco
    drawer.left(90)
    drawer.forward(LENGTH_ARESTA)

    # Draw upper line
    drawer.right(90)
    drawer.forward(LENGTH_ARESTA)

    # Adjust position to next letter
    adjustDrawerPosition(drawer)

def adjustDrawerPosition(drawer):
    drawer.penup()

    currentX = drawer.xcor()
    
    drawer.setpos(currentX + LENGTH_ARESTA/2, 0)
    drawer.pendown()

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


drawInitials();


