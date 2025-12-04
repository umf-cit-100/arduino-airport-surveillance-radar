import tkinter
import math
import numpy as np
from utils.Canvas import Canvas

class Radar:

    def __init__(self) -> None:

        self.winHeight = 300
        self.winWidth = 600
        self.radarSize = 500

        self.data = [0] * 181

        self.refreshInterval = 5

        self.needleAngle = 0

        self.root = tkinter.Tk()
        self.root.title("Light Wave Radar")

        self.centralizeWindow()

        # create canvas
        canvasHeight = self.winHeight
        canvasWidth = self.winWidth
        self.myCanvas = tkinter.Canvas(self.root, height=canvasHeight, width=canvasWidth)
        self.myCanvas.configure(bg='black')
        self.myCanvas.pack()

    def centralizeWindow(self):

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (self.winWidth/2))
        y_cordinate = int((screen_height/2) - (self.winHeight/2))

        self.root.geometry("{}x{}+{}+{}".format(self.winWidth, self.winHeight, x_cordinate, y_cordinate))

    def getBottomDimensions(self):
        cx = self.winWidth / 2
        cy = self.winHeight - 20
        return cx, cy

    def getDestination(self, x, y, angle, radius):

        angle = (angle+90) * math.pi / 180

        endX   = x + radius * math.sin(angle)
        endY   = y + radius * math.cos(angle)

        return endX, endY

    def drawRadar(self):

        for x in range(self.radarSize, 0, -100):
            self.drawArcFromBottom(x, x)

        for x in range(0, 180+1, 30):
            self.drawLineFromBottom(x, self.radarSize / 2, "white", 1)
            self.drawTextFromBottom(x, self.radarSize / 2, str(x)+u"\u00b0")

    def drawArcFromBottom(self, width, height):

        cx, cy = self.getBottomDimensions()

        Canvas.drawArc(self.myCanvas, cx-width/2, cy-height/2, width+(cx-width/2), cy+height/2)

    def drawRecFromBottom(self, width=50, height=50):

        cx, cy = self.getBottomDimensions()

        Canvas.drawRec(self.myCanvas, cx-width/2, cy-height, width+(cx-width/2), cy)

    def drawLineFromBottom(self, angle, radius, fill="red", width=1):

        cx, cy = self.getBottomDimensions()

        endX, endY = self.getDestination(cx, cy, angle, radius)

        Canvas.drawLine(self.myCanvas, cx, cy, endX, endY, fill, width)

    def drawTextFromBottom(self, angle, radius, text):

        cx, cy = self.getBottomDimensions()

        endX, endY = self.getDestination(cx, cy, angle, radius+10)

        Canvas.drawText(self.myCanvas, endX, endY, text, 0-(90-angle))

    def drawCircleFromBottom(self, angle, radius):

        cx, cy = self.getBottomDimensions()

        endX, endY = self.getDestination(cx, cy, angle, radius)

        Canvas.drawCircle(self.myCanvas, endX, endY, 2)

    def drawNeedle(self):
        self.drawLineFromBottom(self.needleAngle, self.radarSize / 2)

    def drawData(self):

        for i in range(len(self.data)):
            luminosity = np.interp(self.data[i], [0, 1023],[0, self.radarSize / 2])
            self.drawCircleFromBottom(i, luminosity)

    def update(self):

        Canvas.clearCanvas(self.myCanvas)

        self.drawRadar()

        self.drawNeedle()

        self.drawData()

        self.root.after(self.refreshInterval, self.update)

    def show(self):
        self.root.after(self.refreshInterval, self.update)
        self.root.mainloop()

    def plot(self, angle:int, value:int):

        angle = max(angle, 0)
        angle = min(angle, 180)

        self.data[angle] = value

        self.needleAngle = angle
