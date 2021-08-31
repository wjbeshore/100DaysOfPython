import turtle as t
import random
timmy = t.Turtle()
t.colormode(255)

# Creates random colors
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    print(r + g + b)
    return color
# Changes Speed
timmy.speed("fastest")

# Creates circle then moves heading to create spirograph
for i in range(40):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading()+10)

screen = t.Screen()
screen.exitonclick()