from math import cos, sin, sqrt

def Decompor_vetor_x(angulo, vetor): #Decompoe a velocidade na componente x
  angulo_rad = angulo * (3.14 / 180)
  return vetor * cos(angulo_rad)

def Decompor_vetor_y(angulo, vetor): #Decompoe a velocidade na componente y
  angulo_rad = angulo * (3.14 / 180)
  return vetor * sin(angulo_rad)

def Posicao_x(tempo, velo_x, pos_inicial=0): #Calcula posição em x em um determinado tempo
  return pos_inicial+(velo_x*tempo)
  
def Posicao_y(pos_inicial, tempo, velo_y): #Calcula posição em y em um determinado tempo
  return pos_inicial+(velo_y*tempo)-(9.8/2)*(tempo**2)

def Tempo_no_ar(velo_y): #Calcula tempo que a bola passa no ar
  return (2*velo_y)/9.8

def Calcular_altura(velo_y, pos_inicial): #Calcula altura máxima da bola
  t = velo_y/9.8

  return Posicao_y(pos_inicial,t,velo_y)

def Calcular_Velo_y(velo_y, tempo): #Calcula velocidade em y em um determinado tempo
  return velo_y - (9.8*tempo)

def Modulo(x , y): #calcula o módulo dos termos
  return sqrt(x**2+y**2)

def Alcance(tempo_ar, pos_inicial, velo_x): #Calcula alcance máximo da bola
  return pos_inicial+(velo_x*tempo_ar)