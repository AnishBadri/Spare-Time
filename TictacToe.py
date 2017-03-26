from _ast import In
import sys

def checkstate(game =[], *args):
  for da in ['X','O']:
      hor = True
      ver = True
      dia = True
      for i in range(4):
          for j in range(4):
              if(game[i][j] == da or game[i][j] == 'T'):
                  hor = False
              if(game[j][i] == da or game[j][i] == 'T'):
                  ver = False
          if(hor or ver):
              return da
          if(game[i][j] == da or game[i][j] == 'T'):
              dia = False
      if(dia):
        return da
  for u in range(4):
      for v in range(4):
          if(game[u][v] == '.'):
              return 'Not Completed'

  return 'Draw'


gamenumber = int(sys.stdin.readline())
gamedata = []
for game in range(1,gamenumber+1):
    gamedata = [sys.stdin.readline().strip()for i in range(4) ]
    state = checkstate(gamedata)
    print("Case #" +str(game) +":")
    if(state in ['X','O']):
        print(state+" Won")
    if(state == 'Draw' ):
        print(state)
    if(state == 'Not Completed'):
        print('Game has not completed')


