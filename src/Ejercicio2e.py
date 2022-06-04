from interpreter import draw
from chessPictures import *

myPicture = square.negative()
myPicture = myPicture.join(square)
myPicture = myPicture.horizontalRepeat(3)
draw(myPicture)