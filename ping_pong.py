import turtle
import time

# Set up the screen
def setup_screen():
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    return wn

# Paddle movement functions
def move_paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def move_paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y - 20)

def move_paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def move_paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y - 20)

# Ball movement and collision
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

def check_collisions():
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        update_score("a")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        update_score("b")

def check_paddle_collision():
    global ball_dx, ball_dy
    
    # Paddle A collision (Left paddle)
    if ball.xcor() > -360 and ball.xcor() < -350:
        if paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
            ball.setx(-340)  # Prevent ball from crossing paddle edge
            ball.dx *= -1  # Reverse direction of the ball

            # Check where the ball hits the paddle for vertical bounce
            if ball.ycor() > paddle_a.ycor() + 20:  # Hit the top of the paddle
                ball.dy = abs(ball.dy)
            elif ball.ycor() < paddle_a.ycor() - 20:  # Hit the bottom of the paddle
                ball.dy = -abs(ball.dy)

    # Paddle B collision (Right paddle)
    if ball.xcor() < 360 and ball.xcor() > 350:
        if paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
            ball.setx(340)  # Prevent ball from crossing paddle edge
            ball.dx *= -1  # Reverse direction of the ball

            # Check where the ball hits the paddle for vertical bounce
            if ball.ycor() > paddle_b.ycor() + 20:  # Hit the top of the paddle
                ball.dy = abs(ball.dy)
            elif ball.ycor() < paddle_b.ycor() - 20:  # Hit the bottom of the paddle
                ball.dy = -abs(ball.dy)

# Update the score
def update_score(player):
    global score_a, score_b
    if player == "a":
        score_a += 1
    elif player == "b":
        score_b += 1
    score.clear()
    score.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Set up paddles, ball, and score
def setup_game_elements():
    global paddle_a, paddle_b, ball, score
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("blue")  # Paddle A color
    paddle_a.shapesize(stretch_wid=6, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("red")  # Paddle B color
    paddle_b.shapesize(stretch_wid=6, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    ball = turtle.Turtle()
    ball.speed(0)  # Ball's speed (0 is normal speed)
    ball.shape("circle")  # Change ball shape to circle
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1  # Constant speed in the X direction
    ball.dy = 1  # Constant speed in the Y direction

    score = turtle.Turtle()
    score.speed(0)
    score.color("white")
    score.penup()
    score.hideturtle()
    score.goto(0, 260)
    update_score("")

# Main game loop
def main():
    global score_a, score_b
    score_a = 0
    score_b = 0

    wn = setup_screen()
    setup_game_elements()

    wn.listen()
    wn.onkeypress(move_paddle_a_up, "w")
    wn.onkeypress(move_paddle_a_down, "s")
    wn.onkeypress(move_paddle_b_up, "Up")
    wn.onkeypress(move_paddle_b_down, "Down")

    while True:
        wn.update()
        move_ball()
        check_collisions()
        check_paddle_collision()
        time.sleep(0.01)  # Adds a small delay to control the speed of the game

# Run the game
if __name__ == "__main__":
    main()
