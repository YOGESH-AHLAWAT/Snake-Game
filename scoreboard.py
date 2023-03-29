from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('Blue')
        self.penup()
        self.score = 0
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color('red')
        self.write(f"GAME OVER \n Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
