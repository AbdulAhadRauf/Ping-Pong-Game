from paddle import Paddle
import turtle as t
from balls import Ball
import time 
from scoreboard import ScoreBoard
game_on = True


screen = t.Screen()
screen.setup(800,600)
screen.bgcolor("Black")
screen.title("Ping Pong Game")
screen.tracer(0)


rpaddle = Paddle((380,0))
lpaddle = Paddle((-380,0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(rpaddle.up, "Up")
screen.onkeypress(rpaddle.down, "Down")
screen.onkeypress(lpaddle.up, "w")
screen.onkeypress(lpaddle.down, "s")


while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.MoveBall()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.WallBounce()

    if ball.distance(rpaddle) < 51 and ball.xcor() > 350 or ball.distance(lpaddle) < 51 and ball.xcor() < -350:
        ball.PaddleBounce()

    if ball.xcor() > 380:
        scoreboard.leftgetspoint()
        ball.ResetBall()


    if ball.xcor() < -380:
        scoreboard.rightgetspoint()
        ball.ResetBall()



screen.exitonclick()