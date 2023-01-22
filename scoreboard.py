import turtle as t

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.leftscore = 0
        self.rightscore = 0
        self.ht()
        self.color("white")
        self.penup()
        self.CreateScore()


    def CreateScore(self):
        self.clear()
        self.goto(-100,210)
        self.write(self.leftscore, align= "center" , font = ("Courier", 45, "normal"))
        self.goto(100,210)
        self.write(self.rightscore, align= "center" , font = ("Courier", 45, "normal"))

    
    def leftgetspoint(self):
        self.leftscore += 1
        self.CreateScore()


    def rightgetspoint(self):
        self.rightscore += 1
        self.CreateScore()

