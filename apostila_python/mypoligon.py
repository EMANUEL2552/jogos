import turtle

bob = turtle.Turtle()

"""desenhar um circulo """
def square(t, lengh):

    for i in range(4):
        t.fd(lengh)
        t.lt(90)
def polygon(t, n, lengh):
    angle = 360 / n
    for i in range(n):
        t.fd(lengh)
        t.lt(angle)

polygon(bob, 7, 70)

square(bob, 100)


