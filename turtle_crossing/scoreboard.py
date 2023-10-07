from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """scoreboard keeps track of which level the user is on.
    Every time the turtle does a successful crossing, the level
    increases. When the turtle hits a car, GAME OVER will be displayed
    on the center."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="left", font=FONT)
