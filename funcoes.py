from math import cos, sin


def Decompor_vetor_x(angulo, vetor):
  angulo_rad = angulo * (3.14 / 180)
  return vetor * cos(angulo_rad)


def Decompor_vetor_y(angulo, vetor):
  angulo_rad = angulo * (3.14 / 180)
  return vetor * sin(angulo_rad)


def Posicao_x(tempo, velo_x, pos_inicial=0):
  return pos_inicial+(velo_x*tempo)
  
def Posicao_y(pos_inicial, tempo, velo_y):
  return pos_inicial+(velo_y*tempo)-(9.8/2)*(tempo**2)

def Calcular_altura(velo_y, pos_inicial):
  t = velo_y/9.8

  return Posicao_y(pos_inicial,t,velo_y)