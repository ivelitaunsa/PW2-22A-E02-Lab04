from interpreter import draw
from chessPictures import *

myPicture1 = square
myPicture1 = myPicture1.join(square.negative())
myPicture1 = myPicture1.horizontalRepeat(3)

myPicture2 = square.negative()
myPicture2 = myPicture2.join(square)
myPicture2 = myPicture2.horizontalRepeat(3)

myPictureFinal = myPicture2.up(myPicture1)
draw(myPictureFinal)

