import funcoes
from math import sqrt

velo = float(input("Insira a velocidade inicial do lançamento: (Por favor faça a conversão e insira em m/s): "))
angulo = float(input("Insira o angulo inicial do lançamento: "))
posy = float(input("Insira a altura inicial do lançamento: (Por favor faça a conversão e insira em m): "))

velo_x = funcoes.Decompor_vetor_x(angulo, velo)
velo_y = funcoes.Decompor_vetor_y(angulo, velo)
tempo_ar = funcoes.Tempo_no_ar(velo_y)
alcance = funcoes.Alcance(tempo_ar, 0, velo_x)
altura = funcoes.Calcular_altura(velo_y, posy)

if angulo == 0 and velo_y == 0:
  tempo = sqrt(posy/4.9)
  posx = funcoes.Posicao_x(tempo, velo_x)
  velo_y = funcoes.Calcular_Velo_y(velo_y, tempo)
  print(f"A distancia horizontal é {posx}\n")
  print(f"A velocidade no tempo {tempo} é {velo_y} no eixo y, {velo_x} no eixo x e o módulo vale {funcoes.Modulo(velo_x, velo_y)}\n")
else:

  print(
      f"As componentes da velocidade inicial são: no eixo x = {velo_x} m/s e no eixo y = {velo_y} m/s\n"
  )
  print(f"A bola permanece no ar por {tempo_ar} s\n")
  print(f"O lançamento tem uma altura máxima de {altura} m\n")
  print(f"O lançamento tem um alcance de {alcance} m\n")
  
  while True:
    opcoes = input("""Gostaria de calcular mais alguma coisa:
    1 - Velocidade em um determinado tempo
    2 - Posição em um determinado tempo
    3 - Módulo de um vetor
    4 - Velocidade antes de alcançar o solo
    5 - Velocidade na altura maxima
    0 - Sair do programa\n""")
  
    if opcoes == "1":
      tempo = float(
          input("Insira o tempo em que deseja calcular a velocidade: "))
      veloy_1 = funcoes.Calcular_Velo_y(velo_y, tempo)
  
      print(
          f"A velocidade no tempo {tempo} é {veloy_1} no eixo y, {velo_x} no eixo x e o módulo vale {funcoes.Modulo(velo_x, veloy_1)}"
      )
  
    elif opcoes == "2":
      tempo = float(input("Insira o tempo em que deseja calcular a posição: "))
      posx = funcoes.Posicao_x(tempo, velo_x)
      posy = funcoes.Posicao_y(posy, tempo, velo_y)
  
      print(
          f"A posição no tempo {tempo} é {posx} m no eixo x e no eixo y {posy} m"
      )
  
    elif opcoes == "3":
      x = float(input("Insira o valor do componente x: "))
      y = float(input("Insira o valor do componente y: "))
      print(f"O módulo do vetor é {funcoes.Modulo(x, y)}")
  
    elif opcoes == "4":
      veloy_2 = funcoes.Calcular_Velo_y(velo_y, tempo_ar)
  
      print(
          f"A velocidade antes de alcançar o solo é {velo_x} m/s no eixo x, {veloy_2} m/s no eixo y e o módulo vale {funcoes.Modulo(velo_x, veloy_2)}"
      )
  
    elif opcoes == "5":
      print(
          f"A velocidade na altura máxima é {velo_x} m/s no eixo x e 0 m/s no eixo y e o módulo vale {funcoes.Modulo(velo_x, 0)}"
      )
  
    if opcoes == "0":
      print("Encerrando programa...")
      break
