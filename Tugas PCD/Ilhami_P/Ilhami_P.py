import cv2

citra = cv2.open('icon.png')

hor = citra.size[0]
ver = citra.size[1]

uk = citra.load()

for x in range(hor):
    for y in range(ver):
        R = 255 - uk[x, y][0]
        G = 255 - uk[x, y][1]
        B = 255 - uk[x, y][2]
        uk[x, y] = (R, G, B)

citra.save('hasil.png')