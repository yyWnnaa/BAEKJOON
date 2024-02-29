import sys
r1, s = map(int, sys.stdin.readline().split())
r2 = s*2 - r1
sys.stdout.write(str(r2))