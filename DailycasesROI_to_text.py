import cv2
import numpy as np
from region_of_interest import roi_dailycase
import pytesseract
import re

data_list = []
clean_data = []
cummulativeCasesDict = {
    'kumulatif' : '0',
    "sembuh" : '0',
    "dalam_perawatan" : '0',
    "meninggal" : '0'
}

scale = 100
img = cv2.imread("DailyImages\Test_DataKumulatif.png")
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
dim = (width, height)
img = cv2.resize(img, dim)

imgShow = img.copy()
imgMask = np.zeros_like(imgShow)

for x, r in enumerate(roi_dailycase):
    cv2.rectangle(imgMask, (r[0][0], r[0][1]), (r[1][0], r[1][1]), (255, 0, 0), cv2.FILLED)
    imgShow = cv2.addWeighted(imgShow, 0.99, imgMask, 0.1, 0)
    imgCrop = img[r[0][1]:r[1][1], r[0][0]:r[1][0]]
    data = pytesseract.image_to_string(imgCrop, config='--psm 7')
    data_list.append(data)

print(data_list)
data_str = ' '.join(map(str, data_list))
clean_text = re.findall('[0-9]+', data_str)
###PLEASE DOUBLE CHECK THE ELEMENTS BETWEEN DATA_STR AND CLEAN_TEXT###
result = dict(zip(cummulativeCasesDict, clean_text))
print(result)