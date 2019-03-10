import tkinter

p1 = (50,50)
p2 = (750,550)

r1 = (-10,-10)
r2 = (10,10)

def map_axis(self, a1, a2, b1, b2, point ):
    (a1x, a1y) = a1
    (a2x, a2y) = a2
    (b1x, b1y) = b1
    (b2x, b2y) = b2
    ax = abs(a1x-a2x)
    bx = abs(b1x-b2x)
    ay = abs(a1y-a2y)
    by = abs(b1y-b2y)
    (pointx, pointy) = point
    out = (
          (pointx - min(a1x,a2x) ) * bx/ax + min(b1x, b2x),
          (pointy - min(a1y,a2y) ) * by/ay + min(b1y, b2y)
    )
    return out

root = tkinter.Tk()

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

root.mainloop()
