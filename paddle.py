import turtle as t 
MOVEBY = 15

class Paddle(t.Turtle):

    def __init__(self,paddlepos):
        super().__init__()
        self.thelist = []
        self.paddlepos = paddlepos
        self.CreatePaddle(paddlepos)
        
        
    def CreatePaddle(self,paddlepos):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid = 5 )
        self.setpos(paddlepos)


    def up(self):
        self.goto(self.xcor(), self.ycor()+MOVEBY)
        
    def down(self):
        self.goto(self.xcor(), self.ycor()-MOVEBY)




