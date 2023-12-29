import sys

a = [1, 1, 2, 2, 2, 8]
b = [int(x) for x in sys.stdin.readline().split()]

for i in range(6):
    sys.stdout.write(str(a[i] - b[i]) + ' ')
