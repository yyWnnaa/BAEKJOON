import sys

n, x = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]

for i in a:
    if i < x:
        print(i, end =' ')