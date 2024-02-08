from JES import *
import numpy as np 
from changeBlue import *
from changeGreen import *
from changeRed import *

#main function
def main():


  # I made duplicates everytime i recolor the shirt, if i call the image sequentially and not separately it will overwrite the 2nd image causing it not to change shirt
  myPic = makePicture( "images.jpg")
  writePictureTo( myPic, "slide01.jpg")


  myPic = makePicture( "images.jpg")
  red_To_Black(myPic)
  writePictureTo(myPic,"slide02.jpg")
  
  myPic = makePicture( "images.jpg")
  red_To_Blue(myPic)
  writePictureTo(myPic,"slide03.jpg")

  myPic = makePicture( "images.jpg")
  red_To_Green(myPic)
  writePictureTo(myPic,"slide04.jpg")



 # Using JES function to create GIF at 0.3 milleseconds interval
  writeSlideShowTo( "luffyChangeShirt.gif", 0.3 )
  
  
  width = getWidth(myPic)
  height = getHeight(myPic)
  print("this image has", width, " width"," pixels wide")
  print("this image has ", height," height"," pixels length")



main()

