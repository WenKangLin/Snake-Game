from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))
        self.goto(0, 270)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.teleport(0,0)
        self.write("Game Over!", align='center', font=('Courier', 20, 'bold'))

