from turtle import *
import time


class Watch:
    def __init__(self, format_24h=True):
        self.format_24h = format_24h

    def toggle_format(self):
        self.format_24h = not self.format_24h


class DigitalWatch(Watch):
    def __init__(self, format_24h=True):
        super().__init__(format_24h)

    def show_time(self):
        t = time.localtime()
        if self.format_24h:
            current_time = time.strftime("%H:%M:%S", t)
        else:
            current_time = time.strftime("%I:%M:%S %p", t)

        clear()
        penup()
        goto(0, 0)
        color("black")
        write(current_time, align="center", font=("Courier", 48, "bold"))


screen = Screen()
screen.title("Digital Watch")
screen.bgcolor("lightblue")
tracer(0)

watch = DigitalWatch(format_24h=True)

while True:
    watch.show_time()
    update()
    time.sleep(1)
