from turtle import left, right, forward, shape, penup, pendown
from turtle import exitonclick
shape ("turtle")
from math import sqrt

def domecek (strana):
    """Nakresli domecek na jeden pokyn"""

    forward (strana)
    left (135)
    forward (sqrt (2)* strana)
    right (135)
    forward (strana)
    left (120)
    forward (strana)
    left (120)
    forward (strana)
    left (30)
    forward (strana)
    left (135)
    forward (sqrt (2)* strana)
    right (135)
    forward (strana)
    left (90)
    forward (30)

# print (domecek (50))
# print (domecek (70))
# print (domecek (100))

strana= 20
for rada in range (3):
    print (domecek (strana))
    strana= strana + 15

exitonclick()
