#!/usr/bin/python3

import os
from PIL import Image
# import cv2

def isGrayScale(imgPath):
    # img = cv2.imread(imgPath)
    img = Image.open(imgPath).convert('RGB')
    # img2 = Image.open(imgPath).convert('LA').convert('RGB')
    w = img.width
    h = img.height
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i, j))
            # print(r,g,b)
            # r2,g2,b2 = img2.getpixel((i, j))
            if r != g != b:
                # image is grayscale if it has one channel i.e. same values for red, green and blue
            # if max(r,g,b) - min(r,g,b) > 10:
            # if r!=r2 or g!=g2 or b!=b2:
                return False
    return True

def classify(imageDir, grayscale, color):
    # move all grayscale files to "grayscale" folder only the coloured ones remain
    if not os.path.exists(grayscale):
        os.makedirs(grayscale)

    if not os.path.exists(color):
        os.makedirs(color)

    entries = os.listdir(imageDir)
    for entry in entries:
        if os.path.isdir(imageDir + entry):
            continue
        imgPath = imageDir + entry
        if isGrayScale(imgPath):
            os.rename(imageDir + entry, grayscale + entry)
            print(entry, 'grayscale')
        else:
            os.rename(imageDir + entry, color + entry)
            print(entry, "color")
        # print("Is {} grayscale?".format(entries[0]), isGrayScale(imgPath))
    # print(entries)

imageDir = './images/'
grayscale = imageDir + 'grayscale/'
color = imageDir + 'color/'

classify(imageDir, grayscale, color)
# print(isGrayScale('./images/14.jpg'))