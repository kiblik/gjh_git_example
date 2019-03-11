class helper:
    def __init__(self, canvas, p1, p2, r1, r2):
        self.canvas = canvas
        self.p1 = p1
        self.p2 = p2
        self.r1 = r1
        self.r2 = r2

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
    def init(self):
        self.canvas.create_line( 
            self.map_axis(self.r1, self.r2, self.p1, self.p2, (self.r1[0], 0)),
            self.map_axis(self.r1, self.r2, self.p1, self.p2, (self.r2[0], 0))
         )
        self.canvas.create_line( 
            self.map_axis(self.r1, self.r2, self.p1, self.p2, (0, self.r1[1])),
            self.map_axis(self.r1, self.r2, self.p1, self.p2, (0, self.r2[1]))
         )

        for i in range(0, max(*self.r1,*self.r2)):
            if i < max(self.r1[0],self.r2[0]):
                xe, ye = self.map_axis(self.r1, self.r2, self.p1, self.p2, (i, 0))
                self.canvas.create_line( xe, ye-5, xe, ye+5 )
            if -i > min(self.r1[0],self.r2[0]):
                xe, ye = self.map_axis(self.r1, self.r2, self.p1, self.p2, (-i, 0))
                self.canvas.create_line( xe, ye-5, xe, ye+5 )
            if i < max(self.r1[1],self.r2[1]):
                xe, ye = self.map_axis(self.r1, self.r2, self.p1, self.p2, (0, i))
                self.canvas.create_line( xe-5, ye, xe+5, ye )
            if -i > min(self.r1[1],self.r2[1]):
                xe, ye = self.map_axis(self.r1, self.r2, self.p1, self.p2, (0, -i))
                self.canvas.create_line( xe-5, ye, xe+5, ye )
         

    def draw(self,fcia):

        for px in range(self.p1[0]+1, self.p2[0]):
            px_old = px-1
            rx, junk = self.map_axis(self.p1, self.p2, self.r1, self.r2, (px, 0) )
            rx_old, junk = self.map_axis(self.p1, self.p2, self.r1, self.r2, (px_old, 0) )

            ry = fcia(rx)
            ry_old = fcia(rx_old)

            r = (rx,ry)
            r_old = (rx_old, ry_old)

            junk, py = self.map_axis(self.r1, self.r2, self. p1, self.p2, r)
            junk, py_old = self.map_axis(self.r1, self.r2, self.p1, self.p2, r_old)

            self.canvas.create_line(px,py,px_old,py_old)

