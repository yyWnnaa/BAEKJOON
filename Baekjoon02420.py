import sys
a, b = map(int, sys.stdin.readline().split())
c = a - b

if c < 0:
    d = c - 2 * c
else:
    d = c
#if c < 0:
#    c = c - 2 * c

sys.stdout.write(str(d))