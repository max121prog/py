from tkinter import *
import time
win = Tk()
win.geometry("600x600")
win.title("Тест")
can = Canvas(win, width=500, height=500)
can.pack()
line1 = can.create_line(250, 0, 250, 500, fill="purple")
rect1 = can.create_rectangle(0, 0, 50, 50, fill="red")
a = 450
while a>0:
    can.move(rect1, 0, 1)
    a = a-1
    win.update()
    time.sleep(0.01)
