from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.color text changes colour of scoreboard
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        #sets game over to middle of screen
        self.goto(0,0)
        self.write(f"   G A M E\n   O V E R\n\nFinal Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
