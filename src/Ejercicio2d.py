from interpreter import draw
from chessPictures import *

myPicture = square
squareChange = square
for i in range(7):
  squareChange = squareChange.negative()
  myPicture = myPicture.join(squareChange)
draw(myPicture)
