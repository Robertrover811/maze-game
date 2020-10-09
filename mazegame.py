import turtle 

maze1 = ["x xxxxxx xxx xxx  xxxxx",
        "xx xxx    xxx xxx xxxxx",
        "xx xxx xxxxxx xxx xxxxx",
        "xx     xxxxxx xxx xxxxx",
        "xxxxxx xxxxxx xxx     x",
        "x      xxxx     xxxxx x",
        "x xxxxxxxx xxxx xxxxx x",
        "x xx    xx  xxx xxxxx x",
        "x xx xx   x xx    xxx x",
        "x    xxxx x xx xx xxx x",
        "x xxxxxxx x    x xxx x",
        "x xxxxxrx xx x xx xxx x",
        "x x   xxx xxxx xxx    x",
        "x x xxxxxxxxxx xxxxxxxx",
        "x     xxxxxxxx     xxxx",
        "xx xx xxhixxxxxxxx xxxx",
        "xx xx x  xxxxxxxxx  xxx",
        "xx xx x xxxxxxxxxxx xxx", 
        "xx xyexxxxxxxxxxxxx xxx",
        "xx xxxxx xxxxxx     xxx",
        "xx ytx   xxxxx xxxx xxx",
        "xx xxx xxxxxxx xxxx xxx",
        "xx xxx   xxxx xxxxxxxx",
       "xx   xxd xxxx xxxxxxxxx",
       "xxxx xxx xxxx    xxxxxx",
       "xxxx     xxxx xxxxxxxxx",
       "xxxx xxxxxxxxxxxxxxxxxx",
       "x xx xx   xxxxxxxxxxxxx",
       "x xx xx g xxxxxxxxxxxxx",
       "x xx xx g       xxxxxxx",
       "x    xxxg xxxxx     xxx",
       "xx xxxxx  xx xx xxx xxx",
       "xx xxxx      xx xxx xxx",
       "xx xxxx xxxxxxx xxx xxx",
       "xx xxxxxxxxxxxx xxx xxx",
       "x   x    xxxxxx xxx xxx",
       "xxx x xx xxxxxx xxx xxx",
       "xxx x xx xxxxxxxxxxxxxx",
       "xx    xxxxxxxxxxxxxxxxx",
       "xx xx x   dfa     xfdxx",         
       "xx xx x xxxde fsx xsdfx",
       "xx xx x xxxxx xxx xxxxx",
       "xx            xx  xxxxx",
       "xx xxx xxxxxxxxxxxxxxxx",
       "xx xxx       xxxxxxxxxx",
       "xx    x xxxx  xxxxxxxxx",
       "xxxx xxxxxxxx     xxxxx",
       "xxxx xxxxxxxx xxx xxxxx",
       "xxx xxxx      xxx xxxxx",
       "xxx     xxxxx xxx    xx",
       "xxxxxxx xxxxx xxx xx xx",
       "xxxxxxx xxxxx xxx xx xx",
       "xxxx      xxx xxx xx xx",
       "x xx xxxx xxxxx   xxxxx",
       "x xx xx   xxxxx xxxxxxx",
       "x xx xx xxxxxxx xxxxxxx",
       "x x    xxxxxxxx xxxxxxx",
       "x xxxx xxxx      xxxxxx",
       "x xxxx xxxx xxxxxxxxxxx",
       "xx     xx     xxxxxxxxx",
       "xxxxxx xx xxx xxxxx xxx",
       "xxxxxx    xxx    xx xxx",
       "xxxxxx x xxxxxxx xx xxx",
       "xxxxxx x xxxxxxx xx xxx",
       "xxxxxxxx xxxxxxxx   xxx",
       "xx  xxxx xxxxxxxx xxxxx",
       "xx xxxxx      xxx xx xx",
       "xx xxxxx xxxx xxx xx xx",
       "x    xxx xxx  xxx    xx",
       "x xx x x xxxxxxxx xxxxx",
       "x xx   x xxxx     xxxxx",
       "x xxxxxx xxxx xxxxxxxxx"]  

mazes = [maze1]


def drawSquare():
  for x in range(4) :
    turtle.forward(25)
    turtle.left(90)
    
def drawRow(row):
  for c in row:
    if c != " ":
      drawSquare()
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()

startX = -800
startY = 900

turtle = turtle.Turtle()
turtle.speed(100)
turtle.penup()

turtle.setpos(startX, startY)
turtle.pendown()

for maze in mazes:
  for x in maze:
    drawRow(x)
    turtle.penup()
    startY -= 30
    turtle.setpos(startX, startY)
    turtle.pendown()

  turtle.penup()  
  startY -= 90
  turtle.setpos(startX, startY)
  turtle.pendown() 

turtle.setpos(-800, 900)
turtle.forward(55)
turtle.left(90)
turtle.forward(35)