from turtle import towards
from interpreter import draw
from chessPictures import *

def construirCasilla(pieza, x):
  if(x == 0):
    return square.negative().under(pieza)
  if(x == 1):
    return square.under(pieza)
  return

def construirPeones():
  figura = construirCasilla(pawn, 1)
  i = 0
  while i < 7:
    if i % 2 == 0: 
      figura = figura.join(construirCasilla(pawn, 0))
    else:
      figura = figura.join(construirCasilla(pawn, 1))
    i += 1
  return figura

def construirPrincipal():
  figura = construirCasilla(rock, 0)
  figura = figura.join(construirCasilla(knight, 1))
  figura = figura.join(construirCasilla(bishop, 0))
  figura = figura.join(construirCasilla(queen, 1))
  figura = figura.join(construirCasilla(king, 0))
  figura = figura.join(construirCasilla(bishop, 1))
  figura = figura.join(construirCasilla(knight, 0))
  figura = figura.join(construirCasilla(rock, 1))

  return figura

# Construyendo Filas
whitePawns = construirPeones()
principalWhite = construirPrincipal()
blackPawns = construirPeones().negative()
principalBlack = construirPrincipal().negative()

# Construyendo casillas vacias
filaCasillas = square.join(square.negative()).horizontalRepeat(3)
filaCasillasInv = filaCasillas.verticalMirror()
casillasVacias = filaCasillasInv.up(filaCasillas).verticalRepeat(1)

#Construyendo formaciones
whiteTroup = principalWhite.up(whitePawns)
blackTroup = blackPawns.up(principalBlack)

# Construyendo tabla
table = whiteTroup.up(casillasVacias).up(blackTroup)

draw(table)