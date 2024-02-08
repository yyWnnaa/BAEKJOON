import sys

a, b, c = map(int, sys.stdin.readline().split())

if (a >= b and b >= c) or (c >= b and b >= a):
    sys.stdout.write(str(b))
elif (b >= a and a >= c) or (c >= a and a >= b):
    sys.stdout.write(str(a))
elif (a >= c and c >= b) or (b >= c and c >= a):
    sys.stdout.write(str(c))