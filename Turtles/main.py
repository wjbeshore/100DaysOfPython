import turtle as t
import random
timmy = t.Turtle()
t.colormode(255
                )
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy.speed("fastest")

timmy.circle(100)

screen = t.Screen()
screen.exitonclick()