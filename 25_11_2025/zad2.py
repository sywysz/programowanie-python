import turtle

bok = 200
predkosc = 1

# zolw = turtle.Pen()
# zolw.speed(predkosc)

# # Podpunkt A
# zolw.forward(bok)
# zolw.left(90)
# zolw.forward(bok)
# zolw.left(90)
# zolw.forward(bok)
# zolw.left(90)
# zolw.forward(bok * 2)
# zolw.right(90)
# zolw.forward(bok)
# zolw.right(90)
# zolw.forward(bok)
# zolw.right(90)
# zolw.forward(bok)

# Podpunkt B
import math
turtle.setworldcoordinates(-400, 0, 400, 800)

szerokosc = 600
wysokosc = 200
szer_drzwi = 50
wys_drzwi = 90

# Parter
turtle.forward(szerokosc / 2)
turtle.left(90)
turtle.forward(wysokosc)
turtle.left(90)
turtle.forward(szerokosc)
turtle.left(90)
turtle.forward(wysokosc)
turtle.left(90)
turtle.forward(szerokosc / 2)

# Drzwi
turtle.left(90)
turtle.forward(wys_drzwi)
turtle.right(90)
turtle.forward(szer_drzwi)
turtle.right(90)
turtle.forward(wys_drzwi)

# Ustawienie pod budowę dachu
turtle.up()
turtle.left(90)
turtle.forward((szerokosc / 2) - szer_drzwi)
turtle.left(90)
turtle.forward(wysokosc)
turtle.down()

# Dach
bok_dachu = szerokosc / math.sqrt(2)

turtle.left(45)
turtle.forward(bok_dachu)
turtle.left(90)
turtle.forward(bok_dachu)

turtle.done()

