from turtle import *
import math
import time


class Numbers:

    def __init__(self, x, y, number, color):
        self._x=x
        self._y=y
        self._number=number
        self._color=color

    def draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        write(self._number, font=("Times New Roman", 25, "normal"))

    def show(self):
        self.draw(self._color)

class ClockFace:
    def __init__(self,r, color):
        self._r=r
        self._color=color
    
    def draw(self, color):
        width(4)
        pencolor(color)
        up()
        setpos(0,-self._r)
        down()
        circle(self._r)
        up()

        for i in range(1, 13):
            angle=90-30*i #розташування цифр
            number = str(i)
            radian=math.radians(angle)
            x=self._r*0.85*math.cos(radian)
            y=self._r*0.85*math.sin(radian)
            n=Numbers(x, y, number, "green")
            n.show()

#координати знаходимо за допомогою полярної системи координат
#x=r*cos a
#y=r*sin a

    def show(self):
        self.draw(self._color)

class Hand:
    def __init__(self, l, angle, width, color):
        self._l=l
        self._angle=angle
        self._width=width
        self._color=color
    
    def draw(self, color):
        pencolor(color)
        speed(0)
        penup()
        goto(0, 0)
        pendown()
        width(self._width)
        setheading(90-self._angle)
        forward(self._l)

    def show(self):
        self.draw(self._color)

    def move(self, d_angle):
       
        self._angle+=d_angle
        self.show()

tracer(0)
r=300
c=ClockFace(r, "black")

while True:

    t=time.localtime()
    reset()
    c.show()
    sec_angle=t.tm_sec*6
    min_angle=t.tm_min*6+t.tm_sec*0.1
    hour_angle=(t.tm_hour%12)*30+t.tm_min*0.5+t.tm_sec*(0.5/60)


    hour_hand=Hand(150, hour_angle, 8, "red")
    minute_hand=Hand(175, min_angle, 4, "red")
    second_hand=Hand(200, sec_angle, 2, "red")
    hour_hand.show()
    minute_hand.show()
    second_hand.show()

    update()
    time.sleep(1)
