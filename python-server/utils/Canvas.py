import tkinter

class Canvas:
    
    @staticmethod
    def clearCanvas(c):
        c.delete('all')

    @staticmethod
    def drawCircle(c, x, y, radius):
        x = x - (radius/2)
        y = y - (radius/2)
        c.create_oval(x+radius, y, x, y+radius, fill="white", width=2)

    @staticmethod
    def drawArc(c, x0, y0, x1, y1):
        c.create_arc(x0, y0, x1, y1, start=0, width=0, extent=180, fill="#2E6B6F", style=tkinter.CHORD)

    @staticmethod
    def drawLine(c, startX, startY, endX, endY, fill="red", width=1):
        c.create_line(startX, startY, endX, endY, fill=fill, width=width)

    @staticmethod
    def drawRec(c, x0, y0, x1, y1):
        c.create_rectangle(x0, y0, x1, y1, fill="blue", outline = 'red')

    @staticmethod
    def drawText(c, x=10, y=10, text="", angle=0, font="Times 10"):
        c.create_text(x, y, fill="white", font=font, text=text, angle=angle)
