from region_of_interest import roi
import pytesseract
import cv2
import numpy as np
from datetime import date
import re

data_list = []
clean_data = []
subdistrictDict = {
    "sagulung" : '0',
    "bulang" : '0',
    "batu_aji" : '0',
    "belakang_padang" : '0',
    "sekupang" : '0',
    "lubuk_baja" : '0',
    "batu_ampar" : '0',
    "bengkong" : '0',
    "nongsa" : '0',
    "batam_kota" : '0',
    "galang" : '0',
    "sei_beduk" : '0',
}

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ACER RYZEN\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

today = date.today()
img = cv2.imread("DailyImages\Subdistrict\datakecamatan_2021-08-27.png")
imgShow = img.copy()
imgMask = np.zeros_like(imgShow)

for x, r in enumerate(roi):
    cv2.rectangle(imgMask, (r[0][0], r[0][1]), (r[1][0], r[1][1]), (255, 0, 0), cv2.FILLED)
    imgShow = cv2.addWeighted(imgShow, 0.99, imgMask, 0.1, 0)
    imgCrop = img[r[0][1]:r[1][1], r[0][0]:r[1][0]]
    data = pytesseract.image_to_string(imgCrop, config='--psm 13 --oem 3')
    data_list.append(data)

print(data_list)
data_str = ' '.join(map(str, data_list))
clean_text = re.findall('[0-9]+', data_str)
###PLEASE DOUBLE CHECK THE ELEMENTS BETWEEN DATA_STR AND CLEAN_TEXT###
result = dict(zip(subdistrictDict, clean_text))
print(result)