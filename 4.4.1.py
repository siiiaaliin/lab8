from turtle import *
import math
import time

class Watch:
    def __init__(self, radius, face_color="black", number_color="green"):
        self._radius = radius
        self._face_color = face_color
        self._number_color = number_color

    def draw_face(self):
        width(4)
        pencolor(self._face_color)
        up()
        setpos(0, -self._radius)
        down()
        circle(self._radius)
        up()

        for i in range(1, 13):
            angle = 90 - 30 * i
            radian = math.radians(angle)
            x = self._radius * 0.85 * math.cos(radian)
            y = self._radius * 0.85 * math.sin(radian)
            self.draw_number(x, y, str(i))

    def draw_number(self, x, y, number):
        pencolor(self._number_color)
        up()
        setpos(x, y)
        down()
        write(number, align="center", font=("Times New Roman", 25, "normal"))

class AnalogWatch(Watch):
    def __init__(self, radius):
        super().__init__(radius)

    def draw_hand(self, length, angle, width_size, color):
        pencolor(color)
        width(width_size)
        penup()
        goto(0, 0)
        setheading(90 - angle)
        pendown()
        forward(length)
        penup()

    def show_time(self):
        t = time.localtime()
        reset()
        self.draw_face()

        sec_angle = t.tm_sec * 6
        min_angle = t.tm_min * 6 + t.tm_sec * 0.1
        hour_angle = (t.tm_hour % 12) * 30 + t.tm_min * 0.5 + t.tm_sec * (0.5 / 60)

        self.draw_hand(150, hour_angle, 8, "red")
        self.draw_hand(175, min_angle, 4, "blue")
        self.draw_hand(200, sec_angle, 2, "green")

class DigitalWatch(Watch):
    def __init__(self, radius, format_24h=True):
        super().__init__(radius)
        self.format_24h = format_24h

    def show_time(self):
        t = time.localtime()
        if self.format_24h:
            current_time = time.strftime("%H:%M:%S", t)
        else:
            current_time = time.strftime("%I:%M:%S %p", t)

        up()
        goto(0, -self._radius - 50) 
        color("black")
        write(current_time, align="center", font=("Courier", 36, "bold"))

screen = Screen()
screen.title("Analog and Digital Watch")
screen.bgcolor("lightblue")
tracer(0)

analog_watch = AnalogWatch(200)  
digital_watch = DigitalWatch(200, format_24h=True)

while True:
    reset()

    analog_watch.show_time()

    digital_watch.show_time()

    update()
    time.sleep(1)

