import turtle as t 

MOVEBY = 10


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.Createball()
        self.move_x = MOVEBY
        self.move_y = MOVEBY
        self.movespeed = 0.1


    def Createball(self):
        self.shape("circle")
        self.color("blue")
        self.penup()

    def MoveBall(self):
        new_x = self.xcor()+ self.move_x
        new_y = self.ycor()+ self.move_y
        self.goto(new_x, new_y)


    def WallBounce(self):
        self.move_y *= -1
   
    
    def PaddleBounce(self):
        self.move_x *= -1
        self.movespeed *= 0.9

    def ResetBall(self):
        self.home()
        self.PaddleBounce()
        self.movespeed = 0.1