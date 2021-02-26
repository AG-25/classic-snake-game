from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        with open("data.txt") as file:
            contents = file.read()
            self.high_score = int(contents[-1])
        super().__init__()
        self.hideturtle()
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Your score is: {self.score}, "
            f"High score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
