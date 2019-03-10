import tkinter
import math
import helpers

p1 = (50,50)
p2 = (750,550)

r1 = (-10,-10)
r2 = (10,10)

root = tkinter.Tk()

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

h = helpers.helper(canvas, p1, p2, r1, r2)

h.init()

h.draw(math.sin)
root.mainloop()
