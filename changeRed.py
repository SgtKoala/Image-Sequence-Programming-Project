from JES import *
from PIL import Image

def red_To_Black(picture):
    for pixel in getPixels(picture):
        # this loop just identifies where and what color are we gonna change which we have here a dominant color red
        if getRed(pixel) > 150 and getGreen(pixel) < 100 and getBlue(pixel) < 100:
            # Change the color to black
            setColor(pixel, makeColor(0, 0, 0))