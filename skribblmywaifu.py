from pynput.mouse import Listener, Button,  Controller
import time
import sys
from PIL import Image

canvas = [[int(sys.argv[1]),int(sys.argv[2])], [int(sys.argv[3]),int(sys.argv[4])]]
# Generate Rectangle
#(width, height)
#PointUpLeft = normal
#PointUpRight = PointUpLeftY & PointDownRightX
#PointDownLeft = PointUpLeftX & PointDownRightY
#PointDownRight = normal
imgSizeX = canvas[1][0] - canvas[0][0]
imgSizeY = canvas[1][1] - canvas[0][1]

def convertImage():
    temp = Image.open('waifu.jpg')
    convert = temp.convert('L')
    bw = convert.point(lambda x: 0 if x<128 else 255, '1')
    bw = bw.resize((imgSizeX,imgSizeY),Image.ANTIALIAS)
    finish = bw.convert('RGB')
    return finish


mouse = Controller()
img = convertImage()
pixels = list(img.getdata())

def pixelsToCordinate():
    pixelMap = []
    value = 0
    tempRow = []
    while value != len(pixels):
        if value % imgSizeX == 0 and value != 0:
            pixelMap.append(tempRow)
            tempRow = []
        tempRow.append(pixels[value][0])
        value += 1
    return pixelMap

def betaBot():
    time.sleep(4.0)
    pixelMap = pixelsToCordinate()
    while(mouse.position[0] != canvas[0][0] or mouse.position[1] != canvas[0][1]):
        mouse.move(canvas[0][0] - mouse.position[0], canvas[0][1] - mouse.position[1])
    time.sleep(1.0)
    #Faster All 3 Lines were drawn
    for pixelRaw in range(0,len(pixelMap)):
        if pixelRaw > 0:
            mouse.release(Button.left)
            mouse.move(canvas[0][0] - mouse.position[0],1)
        for pixel in range(0,len(pixelMap[0])):
            if pixel == 0 and pixelMap[pixelRaw][pixel] == 0:
                mouse.press(Button.left)
            elif pixel != 0 and pixelMap[pixelRaw][pixel] == 0 and pixelMap[pixelRaw][pixel-1] == 255:
                mouse.press(Button.left)
            elif pixel+1 < len(pixelMap[0]) and pixelMap[pixelRaw][pixel+1] == 255 and pixelMap[pixelRaw][pixel] == 0:
                mouse.release(Button.left)
            mouse.move(1,0)
    #Progressive every line is drawn
    #value = 0
    #for pixelRow in pixelMap:
    #    for pixel in pixelRow:
    #        #Enter new line every imgSizeY
    #        if value % imgSizeX == 0:
    #            mouse.move(canvas[0][0] - mouse.position[0],1)
            #SlowDown to prevent lag
            #if value % 300 == 0 and pixel == 0:
            #    time.sleep(0.2)
            #Draw
    #        if pixel == 0:
    #            mouse.click(Button.left,1)
    #        mouse.move(1,0)
    #        value +=1
    exit()
betaBot()