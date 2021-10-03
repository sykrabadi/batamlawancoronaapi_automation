"""
import cv2

scale = 1.1
circles = []
counter = 0
counter2 = 0
point1 = []
point2 = []
myPoints = []
myColor = []

def mousePoints(event, x, y, flags, params):
    global counter, point1, point2, counter2, circles, myColor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter == 0:
            point1 = int(x//scale), int(y//scale)
            counter += 1
            myColor = (255, 0, 0)
        elif counter == 1:
            point2 = int(x//scale), int(y//scale)
            name = input('Enter Name : ')
            myPoints.append([point1, point2, name])
            counter = 0
        circles.append([x, y, myColor])
        counter2 *= 1
    

img = cv2.imread("DailyImages\Test_DataKumulatif.png")
img = cv2.resize(img, (0,0), None, scale, scale)
while True:
    for x, y, color in circles:
        cv2.circle(img, (x, y), 3, color, cv2.FILLED)
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        print(myPoints)
        break
"""

#After extracting manually, ROI are shown below

roi = [
    [(520, 581), (560, 597), '1'], 
    [(136, 508), (170, 523), '2'], 
    [(136, 405), (181, 421), '3'], 
    [(137, 289), (171, 305), '4'], 
    [(307, 173), (346, 189), '5'], 
    [(435, 193), (479, 211), '6'], 
    [(621, 152), (668, 169), '7'], 
    [(932, 227), (981, 242), '8'], 
    [(1004, 281), (1052, 299), '9'], 
    [(1005, 416), (1052, 433), '10'], 
    [(1004, 555), (1039, 570), '11'], 
    [(698, 582), (742, 595), '12']]

roi_dailycase = [[(663, 2), (726, 23), '1'], [(663, 26), (726, 48), '2'], [(665, 50), (727, 73), '3'], [(665, 72), (727, 96), '4']]