
import turtle

window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color(input("Escoge el color de la paleta 1"))
paddle_a.shapesize(stretch_wid=7, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color(input("Escoge el color de la paleta 2"))
paddle_b.shapesize(stretch_wid=7, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color(input("Escoge el color de la bola"))
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dy = 1
ball.dx = 1

# Scoreboard
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()

    if(y < 210):
        y +=20

    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()

    if(y > -210):
        y -=20

    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()

    if(y < 210):
        y +=20

    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()

    if(y > -210):
        y -=20

    paddle_b.sety(y)


window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

while score_a < 10 and score_b < 10: 
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = 1

    if ball.xcor() > 390:
        score_a = score_a + 1
        score.clear()
        score.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        ball.setx(390)
        ball.goto(0,0)
        ball.dx = -1

    if ball.xcor() < -390:
        score_b = score_b + 1
        score.clear()
        score.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        ball.setx(-390)
        ball.goto(0,0)
        ball.dx = 1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx = 1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx = -1

