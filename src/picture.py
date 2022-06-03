from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for value in self.img:
      horizontal.insert(0,value) 
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for value in self.img:
      valueNeg = ""
      for caracter in value:
        valueNeg += self._invColor(caracter)
      negative.append(valueNeg)

    return Picture(negative)

  def join(self, p):
    joinRslt = []
    i = 0
    while i<len(self.img):
      joinRslt.append(self.img[i] + p.img[i])
      i+=1
    return Picture(joinRslt)

  def up(self, p):
    upPict = []
    for value in p.img:
      upPict.append(value)
    for value in self.img:
      upPict.append(value)
    return Picture(upPict)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    result = []
    upperIMG = p.img
    underIMG = self.img
    for i in range(len(upperIMG)):
        txt = ""
        for j in range(len(upperIMG)):
            if upperIMG[i][j] != underIMG[i][j] and upperIMG[i][j] != " ":
                txt += upperIMG[i][j]
            else:
                txt += underIMG[i][j]
        result.append(txt)
    return Picture(result)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeat = self.img
    funcConcatenar = lambda a, b : a + b
    i = 0
    while i < n:
        repeat = map(funcConcatenar, repeat, self.img)
        i += 1
    return Picture(list(repeat))
    

  def verticalRepeat(self, n):
    repeat = self.img
    i = 0
    while i < n:
        repeat = repeat + self.img
        i += 1
    return Picture(repeat)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotate = []
    # Creating all elements of the list
    for value in self.img[0]:
      rotate.append(value)

    i=1; j=0
    while i<len(self.img):
      while j<len(self.img[i]):
        rotate[j] = self.img[i][j] + rotate[j]
        j+=1
      j=0
      i+=1

    return Picture(rotate)

