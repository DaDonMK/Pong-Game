from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# listen for key strokes
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
score = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    # detect collision w wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision w paddle
    if ball.distance(r_paddle) < 70 and ball.xcor() > 340 or ball.distance(l_paddle) < 70 and ball.xcor() < -340:
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 370:
        ball.reset_position()
        score.l_point()

    # detect l paddle misses
    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()



screen.exitonclick()
