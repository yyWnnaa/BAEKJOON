import sys

hap, cha = map(int, sys.stdin.readline().split())

winS = (hap + cha) // 2
loseS = hap - winS

sys.stdout.write(str(winS) + ' ' + str(loseS))