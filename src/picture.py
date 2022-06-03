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
    return Picture(None)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, p):
      joinRslt = []
      i = 0
      while i<len(self.img):
          joinRslt.append(self.img[i] + p[i])
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
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

