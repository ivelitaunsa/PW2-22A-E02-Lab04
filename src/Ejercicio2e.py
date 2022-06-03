from interpreter import draw
from chessPictures import *

myPicture = square.negative()
myPicture = myPicture.join(square)
draw(myPicture)