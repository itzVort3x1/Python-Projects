from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import  time

tim  = Turtle()


screen = Screen()
screen.bgcolor("black")
screen.setup(width= 1100, height= 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((530, 0))
l_paddle = Paddle((-540, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with r_paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 340 or ball.distance(l_paddle) < 30 and ball.xcor() < -340:
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 550:
        ball.reset_position()
        scoreboard.l_point()

    #detect when left paddle misses
    if ball.xcor() < -550:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()