"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

import random
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['blue', 'yellow', 'magenta', 'orange', 'dark green']

snakeColor = random.choice([i for i in colors])
foodColor = random.choice([j for j in colors if j != snakeColor])


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy() # posición antes de moverse
    head.move(aim) # posición después de movimiento
    food.move(vector(random.choice([-10, 0, 10]), random.choice([-10, 0, 10]))) # asignación de posiciones random comida

    # si se sale del tablero o se come a sí misma, se dibuja en rojo la cabeza, se actualiza y termina juego
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    # si la comida no está dentro de límites la reposiciona dentro del tablero de nuevo en posición random
    elif not inside(food):
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10

    snake.append(head) # vector que agrega al cuerpo (posición)

    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
    else:
        snake.pop(0) # se mueve hacia el vector posterior

    clear()
     # Se dibuja la comida en coordenadas correspondientes

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    update()
    ontimer(move, 100) # velocidad de snake


setup(420, 420, 370, 0) # dimensiones tablero
hideturtle()
tracer(False)
listen()
# detección de teclas presionadas
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
