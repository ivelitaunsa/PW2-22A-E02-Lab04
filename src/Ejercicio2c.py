from interpreter import draw
from chessPictures import *

myPicture = queen
for i in range(3):
  myPicture = myPicture.join(queen)
draw(myPicture)
