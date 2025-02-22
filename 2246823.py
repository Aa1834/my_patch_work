from graphics2 import *
from array import *

def execute(win,x,y,colours):
    
    #testing edit
    firstTile(win,x,y,colours)
    drawCircle(win,x,y,colours)
    secondTile(win,x,y,colours)
    lastTile(win,x,y,colours)
    thirdTile(win,x,y,colours)
    fourthTile(win,x,y,colours)
    
    startingPoint = Point(x,y)
    endPoint= Point(x + 100,y+100)
    
    rectangle = Rectangle(startingPoint,endPoint)
    rectangle.setWidth(1)
    rectangle.setOutline("black")
    rectangle.draw(win)
    
def getMatrix(columns):
    
    fiveByFive=  [['S','S','S','S','S'], ['P1','S','S','S','P11'],['P1','P1','P2','P11','P11'],['S11','P2','P2','P2','S12'],['P2','P2','P2','P2','P2']]
    sevenBySeven=  [['S','S','S','S','S','S','S'],
                    ['P1','S','S','S','S','S','P11'],
                    ['P1','P1','S','S','S','P11','P11'],
                    ['P1','P1','P1','P2','P11','P11','P11'],
                    ['S11','S11','P2','P2','P2','S12','S12'],
                    ['S11','P2','P2','P2','P2','P2','S12'],
                    ['P2','P2','P2','P2','P2','P2','P2']]
    nineByNine=   [['S','S','S','S','S','S','S','S','S'],
                    ['P1','S','S','S','S','S','S','S','P11'],
                    ['P1','P1','S','S','S','S','S','P11','P11'],
                    ['P1','P1','P1','S','S','S','P11','P11','P11'],
                    ['P1','P1','P1','P1','P2','P11','P11','P11','P11'],
                    ['S11','S11','S11','P2','P2','P2','S12','S12','S12'],
                    ['S11','S11','P2','P2','P2','P2','P2','S12','S12'],
                    ['S11','P2','P2','P2','P2','P2','P2','P2','S12'],
                    ['P2','P2','P2','P2','P2','P2','P2','P2','P2']]
    if columns==5:
        return fiveByFive
    elif columns==7:
        return sevenBySeven
    elif columns==9:
        return nineByNine
    
    
    

def drawTopRow(win, column, colours):
    tileSizeX=0
    tileSizeY=0
    patternToFill=getMatrix(column)
    
    #drawSecondRow(win,column, colours, tileSizeX, tileSizeY)
    
    startX=0
    startY=0
    startPoint=Point(startX,startY)
    boxSize=100
    endPoint=Point(100,100)
    for row in patternToFill:
        endPoint=Point(startX+boxSize, startY+boxSize)
        startPoint=Point(startX,startY)
        for cell in row:   
            if cell=='S':               
                square = Rectangle(startPoint, endPoint)
                square.setFill(colours[0])
                square.setOutline('black')
                square.draw(win)
            elif cell=='S11':                
                square = Rectangle(startPoint, endPoint)
                square.setFill(colours[1])
                square.setOutline('black')
                square.draw(win)
            elif cell=='S12':                
                square = Rectangle(startPoint, endPoint)
                square.setFill(colours[2])
                square.setOutline('black')
                square.draw(win)
            elif cell=='P1':               
                drawSecondRow(win,column, colours[1], startX, startY)
            elif cell=='P11':               
                drawSecondRow(win,column, colours[2], startX, startY)
            elif cell=='P2':
                drawSquare2(win,startX,startY,colours[0])
                
            startX = startX + 100            
            startPoint=Point(startX,startY)
            endPoint=Point(startX + 100,startY + 100)
        startY = startY + 100
        startX = 0
        
            

    win.getMouse()


def drawSquare2(win, x, y,colours):
    win.setBackground("white")
    
    startingPoint = Point(x,y)
    endPoint= Point(x + 100,y+100)
    
    rectangle = Rectangle(startingPoint,endPoint)
    rectangle.setWidth(1)
    rectangle.setOutline("black")
    rectangle.draw(win)
    
    difference = 10

    x1 = 0 + x
    y1 = 90 + y

    x2 = x1 + difference
    y2 = y1 + difference

    topLeft = Point(x1, y1)
    bottomRight = Point(x2, y2)

    square = Rectangle(topLeft, bottomRight)
    square.setFill("blue")
    square.draw(win)

    x3 = x1 + 10
    y3 = y1 - 10

    x4 = x2 + 10
    y4 = y2 - 10

    for i in range(9):
        topLeftRepeated = Point(x3, y3)
        bottomRightRepeated = Point(x4, y4)

        repeatedSquares = Rectangle(topLeftRepeated, bottomRightRepeated)
        repeatedSquares.setFill("blue")
        repeatedSquares.draw(win)

        x3 = x3 + 10
        y3 = y3 - 10
        x4 = x4 + 10
        y4 = y4-10
    
def drawSecondRow(win, column, colours, x,y):
    
     execute(win,x,y,colours)
 
        



def firstTile(win,x,y, colours):
    x1 = 0 + x
    y1 = 0 + y
    
    x2 = 20 + x
    y2 = 20 + y
    
    topLeft = Point(x1, y1)
    bottomRight = Point(x2, y2)
    
    square = Rectangle(topLeft, bottomRight)
    square.setFill(colours)
    square.setOutline(colours)
    square.draw(win)
    
    y3 = y1 + 20
    
    y4 = y2 + 20
    
    for i in range(4):
        #new repeated top left corner for each of the 4 red tiles (squares).
        
        
        topLeftRepeated = Point(x1,y3)
        bottomRightRepeated = Point(x2,y4)
        
        
        repeatedSquare = Rectangle(topLeftRepeated,bottomRightRepeated)
        repeatedSquare.setFill(colours)
        repeatedSquare.setOutline(colours)
        repeatedSquare.draw(win)
        
        
        y3 = y3 + 20
        
        y4 = y4 + 20
        
    
def drawCircle(win, x,y,colours):
    x1 = 60 + x
    y1 = 0 + y
    
    x2 = 80 + x
    y2 = 20 + y

    topLeft = Point(x1, y1)
    bottomRight = Point(x2, y2)
    
    square = Rectangle(topLeft, bottomRight)
    square.setFill("white")
    square.draw(win)
    
    
    y3 = y1 + 40
    
    y4 = y2 + 40
    
    topLeftCorner = Point(x1,y3)
    bottomRightCorner = Point(x2,y4)
    
    for i in range(2):
        repeatedTile = Rectangle(topLeftCorner,bottomRightCorner)
        repeatedTile.setOutline("White")
        repeatedTile.setFill("white")
        y3 = y3 + 40
        y4 = y4 + 40
        repeatedTile.draw(win)
        topLeftCorner = Point(x1,y3)
        bottomRightCorner = Point(x2,y4) 
    
    x1 = 10 + x
    y1 = 10 + y
    centre = Point(x1,y1)
    radius = 5
    circle = Circle(centre,radius)
    circle.setOutline("white")
    circle.setFill("white")
    circle.draw(win)
    
    y2 = y1 + 20
    
    
    for i in range(4):
        repeatedCircle = Circle(Point(x1,y2),radius)
        repeatedCircle.setOutline("white")
        repeatedCircle.setFill("white")
        repeatedCircle.draw(win)        
        
        y2 = y2 + 20
               
    
def secondTile(win, x,y,colours):
    
    x1 = 20 + x
    y1 = 0 + y
    
    x2 = 40 + x
    y2 = 20 + y

    topLeft = Point(x1, y1)
    bottomRight = Point(x2, y2)
    
    square = Rectangle(topLeft, bottomRight)
    square.setFill("white")
    square.setOutline("white")
    square.draw(win)
    
    
    y3 = y1 + 40
    
    y4 = y2 + 40
    
    topLeftCorner = Point(x1,y3)
    bottomRightCorner = Point(x2,y4)
    
    for i in range(2):
        repeatedTile = Rectangle(topLeftCorner,bottomRightCorner)
        repeatedTile.setOutline("White")
        repeatedTile.setFill("white")
        y3 = y3 + 40
        y4 = y4 + 40
        repeatedTile.draw(win)
        
        
        topLeftCorner = Point(x1,y3)
        bottomRightCorner = Point(x2,y4)
        drawTriangle(win,x,y,colours)
        drawInnerCircle(win,x,y)
        remainingTiles(win,x,y,colours)
        
    
    
    
    
    
def drawTriangle(win,x,y,colours):
    x1 = 30 + x
    y1 = 0 + y
    
    x2 = 20 + x
    y2 = 10 + y
    
    x3 = 40 + x
    y3 = 10 + y
    
    x4 = 30 + x
    y4 = 20 + y
    
    topCorner = Point(x1,y1)
    leftCorner = Point(x2,y2)
    rightCorner = Point(x3,y3)
    bottomCorner = Point(x4,y4)
    
    polygon1 = Polygon(topCorner,leftCorner,rightCorner)
    polygon2 = Polygon(bottomCorner, leftCorner,rightCorner)
    
    polygon1.draw(win)
    polygon2.draw(win)
    
    polygon1.setFill(colours)
    polygon2.setFill(colours)
    
    polygon1.setOutline(colours)
    polygon2.setOutline(colours)
    
    y5 = y1 + 40
    y6=  y2 + 40
    y7 = y3 + 40
    y8 = y4 + 40
    
    top = Point(x1,y5)
    left = Point(x2,y6)
    right = Point(x3,y7)
    bottom = Point(x4,y8)
    
    for i in range(2):
        
        top = Point(x1,y5)
        left = Point(x2,y6)
        right = Point(x3,y7)
        bottom = Point(x4,y8)
        
        polygon3 = Polygon(top,left,right)
        polygon3v2 = Polygon(bottom,left,right)
        polygon3.setFill(colours)
        polygon3.setOutline(colours)
        polygon3v2.setFill(colours)
        polygon3v2.setOutline(colours)
        polygon3.draw(win)
        polygon3v2.draw(win)
        
        y5 = y5+40
        y6 = y6+40
        y7 = y7+40
        y8 = y8+40
        
        """x1= x1 + 40
        x2= x2 + 40
        x3 = x3 + 40
        x4 = x4 + 40"""
        
        top = Point(x1,y5)
        left = Point(x2,y6)
        right = Point(x3,y7)
        bottom = Point(x4,y8)
    
    
    
   
    
def drawInnerCircle(win, x,y):
    x1 = 30 + x
    y1 = 10 + y
    centre = Point(x1,y1)
    radius = 5
    circle = Circle(centre,radius)
    circle.setOutline("white")
    circle.setFill("white")
    circle.draw(win)
    
    y2 = y1 + 40
    
    
    for i in range(2):
        repeatedCircle = Circle(Point(x1,y2),radius)
        repeatedCircle.setOutline("white")
        repeatedCircle.setFill("white")
        repeatedCircle.draw(win)
        y2 = y2+40
    
    
    
    


def lastTile(win,x,y,colours):
    x1 = 80 + x
    y1 = 0 + y
    x2= 100 + x
    y2 = 20 + y
    
    topLeftCorner = Point(x1,y1)
    bottomRightCorner = Point(x2,y2)
    square = Rectangle(topLeftCorner,bottomRightCorner)
    square.setFill(colours)
    square.setOutline(colours)
    square.draw(win)
    
    y3 = y1+20
    y4 = y2+20
    
    for i in range(4):
    
        topLeftRepeated = Point(x1,y3)
        bottomRightRepeated = Point(x2,y4)
        
        repeatedlastTile = Rectangle(topLeftRepeated, bottomRightRepeated)
        repeatedlastTile.setFill(colours)
        repeatedlastTile.setOutline(colours)
        repeatedlastTile.draw(win)
        
        y3 = y3 +20
        y4 = y4+20
        drawLastCircles(win,x,y)

def drawLastCircles(win,x,y):
    x1 = 90 + x
    y1 = 10 + y
    centre = Point(x1,y1)
    radius = 5
    circle = Circle(centre,radius)
    circle.setOutline("white")
    circle.setFill("white")
    circle.draw(win)
    
    y2 = y1 + 20
    
    
    for i in range(4):
        repeatedCircle = Circle(Point(x1,y2),radius)
        repeatedCircle.setOutline("white")
        repeatedCircle.setFill("white")
        repeatedCircle.draw(win)
        
        
        y2 = y2 + 20

def thirdTile(win,x,y,colours):
    x1 = 40 + x
    y1 = 0 + y
    x2 = 60 + x
    y2 = 20 + y
    
    topLeftCorner = Point(x1,y1)
    bottomRightCorner = Point(x2,y2)
    square = Rectangle(topLeftCorner,bottomRightCorner)
    square.setFill(colours)
    square.setOutline(colours)
    square.draw(win)
    
    y3 = y1+20
    y4 = y2+20
    
    for i in range(4):
    
        topLeftRepeated = Point(x1,y3)
        bottomRightRepeated = Point(x2,y4)
        
        repeatedlastTile = Rectangle(topLeftRepeated, bottomRightRepeated)
        repeatedlastTile.setFill(colours)
        repeatedlastTile.setOutline(colours)
        repeatedlastTile.draw(win)
        
        y3 = y3+20
        y4 = y4+20
        drawThirdCircles(win,x,y)
        
        

def drawThirdCircles(win, x,y):
    x1 = 50 + x
    y1 = 10 + y
    centre = Point(x1,y1)
    radius = 5
    circle = Circle(centre,radius)
    circle.setOutline("white")
    circle.setFill("white")
    circle.draw(win)
    
    y2 = y1 + 20
    
    
    for i in range(4):
        repeatedCircle = Circle(Point(x1,y2),radius)
        repeatedCircle.setOutline("white")
        repeatedCircle.setFill("white")
        repeatedCircle.draw(win)
        y2 = y2+20


def fourthTile(win, x,y,colours):
    x1 = 60 + x
    y1 = 0 + y
    
    x2 = 80 + x
    y2 = 20 + y

    topLeft = Point(x1, y1)
    bottomRight = Point(x2, y2)
    
    square = Rectangle(topLeft, bottomRight)
    square.setFill("white")
    square.setOutline("white")
    square.draw(win)
    
    
    y3 = y1 + 40
    
    y4 = y2 + 40
    
    topLeftCorner = Point(x1,y3)
    bottomRightCorner = Point(x2,y4)
    
    for i in range(2):
        repeatedTile = Rectangle(topLeftCorner,bottomRightCorner)
        #repeatedTile.setOutline("White")
        repeatedTile.setFill("white")
        repeatedTile.setOutline("white")
        y3 = y3 + 40
        y4 = y4 + 40
        repeatedTile.draw(win)
        
        
        topLeftCorner = Point(x1,y3)
        bottomRightCorner = Point(x2,y4)
        drawSecondTriangle(win,x,y,colours)
        drawFourthCircle(win,x,y,colours)
        fourthRowRedTiles(win,x,y,colours)
        fourthRowCircles(win,x,y,colours)
    
def drawSecondTriangle(win,x,y,colours):
    x1 = 70 + x
    y1 = 0 + y
    
    x2 = 60 + x
    y2 = 10 + y
    
    x3 = 80 + x
    y3 = 10 + y
    
    x4 = 70 + x
    y4 = 20 + y
    
    topCorner = Point(x1,y1)
    leftCorner = Point(x2,y2)
    rightCorner = Point(x3,y3)
    bottomCorner = Point(x4,y4)
    
    polygon1 = Polygon(topCorner,leftCorner,rightCorner)
    polygon2 = Polygon(bottomCorner, leftCorner,rightCorner)
    
    polygon1.draw(win)
    polygon2.draw(win)
    
    polygon1.setFill(colours)
    polygon2.setFill(colours)
    
    polygon1.setOutline(colours)
    polygon2.setOutline(colours)
    
    y5 = y1+40
    y6= y2+40
    y7 = y3+40
    y8 = y4 + 40
    
    top = Point(x1,y5)
    left = Point(x2,y6)
    right = Point(x3,y7)
    bottom = Point(x4,y8)
    
    for i in range(2):
        
        top = Point(x1,y5)
        left = Point(x2,y6)
        right = Point(x3,y7)
        bottom = Point(x4,y8)
        
        polygon3 = Polygon(top,left,right)
        polygon3v2 = Polygon(bottom,left,right)
        polygon3.setFill(colours)
        polygon3.setOutline(colours)
        polygon3v2.setFill(colours)
        polygon3v2.setOutline(colours)
        polygon3.draw(win)
        polygon3v2.draw(win)
        
        y5 = y5+40
        y6 = y6+40
        y7 = y7+40
        y8 = y8+40
        
    polygon4v2 = Polygon(bottom,right,left)
    polygon4v2.setOutline(colours)
    polygon4v2.setFill(colours)
    polygon4v2.draw(win)
    
def drawFourthCircle(win, x,y,colours):
    x1 = 70 + x
    y1 = 10 + y
    centre = Point(x1,y1)
    radius = 5
    circle = Circle(centre,radius)
    circle.setOutline("white")
    circle.setFill("white")
    circle.draw(win)
    
    y2 = y1 + 40
    
    
    for i in range(2):
        repeatedCircle = Circle(Point(x1,y2),radius)
        repeatedCircle.setOutline("white")
        repeatedCircle.setFill("white")
        repeatedCircle.draw(win)
        
        
        y2 = y2 + 40
        
       
   

def remainingTiles(win,x,y,colours):
    x1 = 20 + x
    y1 = 20 + y
    
    x2 = 40 + x
    y2 = 40 + y

    topLeft = Point(x1, y1)
    bottomRight = Point(x2, y2)
    
    square = Rectangle(topLeft, bottomRight)
    square.setFill(colours)
    square.setOutline(colours)
    square.draw(win)
    
    
    y3 = y1 + 40
    
    y4 = y2 + 40
    
    topLeftCorner = Point(x1, y3)
    bottomRightCorner = Point(x2, y4)
    
    for i in range(1):
        repeatedTile = Rectangle(topLeftCorner, bottomRightCorner)
        # repeatedTile.setOutline("White")
        repeatedTile.setFill(colours)
        repeatedTile.setOutline(colours)
        y3 = y3 + 40
        y4 = y4 + 40
        repeatedTile.draw(win)
        
        topLeftCorner = Point(x1, y3)
        bottomRightCorner = Point(x2, y4)
        
    drawRemainderCircle(win, x, y)

def drawRemainderCircle(win, x,y):
    x1 = 30 + x
    y1 = 30 + y
    centre = Point(x1, y1)
    radius = 5
    
    y2 = y1 + 40
    circle = Circle(centre, radius)
    circle.setOutline("white")
    circle.setFill("white")
    circle.draw(win)
    
    for i in range(1):
        repeatedCircle = Circle(Point(x1, y2), radius)
        repeatedCircle.setOutline("white")
        repeatedCircle.setFill("white")
        repeatedCircle.draw(win)
    
        y2 = y2 + 40

def fourthRowRedTiles(win,x,y,colours):
    x1 = 60 + x
    y1 = 20 + y
    
    x2 = 80 + x
    y2 = 40 + y

    topLeft = Point(x1, y1)
    bottomRight = Point(x2, y2)
    
    square = Rectangle(topLeft, bottomRight)
    square.setFill(colours)
    square.setOutline(colours)
    square.draw(win)
    
    
    y3 = y1 + 40
    
    y4 = y2 + 40
    
    topLeftCorner = Point(x1, y3)
    bottomRightCorner = Point(x2, y4)
    
    for i in range(1):
        repeatedTile = Rectangle(topLeftCorner, bottomRightCorner)
        # repeatedTile.setOutline("White")
        repeatedTile.setFill(colours)
        repeatedTile.setOutline(colours)
        y3 = y3 + 40
        y4 = y4 + 40
        repeatedTile.draw(win)
        
        topLeftCorner = Point(x1, y3)
        bottomRightCorner = Point(x2, y4)

def fourthRowCircles(win,x,y,colours):
    x1 = 70 + x
    y1 = 30 + y
    centre = Point(x1, y1)
    radius = 5
    
    circle = Circle(centre, radius)
    circle.setOutline("white")
    circle.setFill("white")
    circle.draw(win)
    
    y2 = y1 + 40
    repeatedCircle = Circle(Point(x1, y2), radius)
    repeatedCircle.setOutline("white")
    repeatedCircle.setFill("white")
    repeatedCircle.draw(win)
    

def main():
    while True:
        column = eval(input("Enter grid size for the column: 5x5 or 7x7 or 9x9 "))
        print("Note that rows and column value must be same else the program won't work")
        if 5 <= column <= 9 and column != 6:
            break
    while True:
        rows = eval(input("Enter grid size for the rows: 5x5, 7x7 or 9x9"))
        if 5 <= rows <= 9 and rows != 6:
            break
    colourSelection = ['blue', 'cyan', 'green', 'red', 'yellow', 'magenta']
    print("Enter colours, in space separated order: cyan blue yellow magenta. Valid colours are: ", colourSelection)
    colours = input("colours: ").split(' ')
    width = column * 100
    height = rows * 100
    
    win = GraphWin("2246823.py", width, height)
    for j in range(3):
        while colours[j] not in colourSelection:
            print("The colour", colours[j], "you have entered is not in the list, please choose again. ")
            colours[j] = input("Select another colour to replace the invalid colour you selected ")
    else:
        colourSelection.remove(colours[j])
    drawTopRow(win, column, colours)
main()
# Call the main function

