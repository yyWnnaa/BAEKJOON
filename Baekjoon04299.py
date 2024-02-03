import sys

hap, cha = map(int, sys.stdin.readline().split())

if hap - cha < 0 or (hap - cha) % 2 != 0:
#  hap + cha < 0 으로 바꾸면 틀림
#                   (hap + cha) % 2 != 0: 으로 바꿔도 맞음
    sys.stdout.write(str(-1))
else:
    winS = (hap + cha) // 2
    loseS = hap - winS
    
    #아래와 같이 하지 않고 max min 함수를 사용해도 된다.
    if loseS > winS:
        temp = loseS
        loseS = winS
        winS = temp
    sys.stdout.write(str(winS) + ' ' + str(loseS))
