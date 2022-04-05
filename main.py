import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

puntaje = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

jugador = Player()
screen.listen()
screen.onkey(jugador.go_up, "Up")
screen.onkey(jugador.go_down, "Down")

carros = CarManager()
tiempo = 0.1

game_is_on = True
while game_is_on:
    time.sleep(tiempo)
    screen.update()
    carros.create_car()
    carros.move_cars()

    for carro in carros.all_cars:
        if carro.distance(jugador) < 20 or jugador.ycor() < -310:
            game_is_on = False
            puntaje.game_over()

    if jugador.finish_line():
        jugador.starting_position()
        carros.level_up()
        puntaje.punto()

screen.exitonclick()
