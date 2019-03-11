import tkinter
import helpers
import fcie

p1 = (50,50)
p2 = (750,550)

r1 = (-10,-10)
r2 = (10,10)

root = tkinter.Tk()

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

h = helpers.helper(canvas, p1, p2, r1, r2)

h.init()

for fcia_name in h.list_fcia():
    def creator(f):
        fcia = getattr(fcie,f)
        def wrapper():
            h.init()
            h.draw(fcia)
        return wrapper
    button = tkinter.Button(root, text = fcia_name, command = creator(fcia_name) )
    button.pack()

root.mainloop()
