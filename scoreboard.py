from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def punto(self):
        self.level += 1
        self.actualizar_puntaje()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
