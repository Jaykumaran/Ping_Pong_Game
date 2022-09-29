from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-140, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(140, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score +=1
        self.update_score()