import sys


def NumberSeperator(n):
    # array = []
    numberarr = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    i = 0
    copy = 0
    final = 0
    rem = 0
    while(True):
        i=i+1
        copy = n *i
        final = copy
        while(copy>0):
            rem = int(copy%10)
            numberarr[rem] = '@'
            copy=int(copy/10)
            if(Checkarray(numberarr)):
                return final
        # print(numberarr)


def Checkarray(numberarr):
    if('.' in numberarr):
        return False
    else:
        return True

# number = int(sys.stdin.readline())
gamenumber = int(sys.stdin.readline())
for i in range(1,gamenumber+1):
    checknum = int(sys.stdin.readline())
    if(checknum!=0):
        print("Case #" + str(i) + ': ' +str(NumberSeperator(checknum)))
    else:
        print("Case #" + str(i) + ': ' + 'INSOMNIA')
