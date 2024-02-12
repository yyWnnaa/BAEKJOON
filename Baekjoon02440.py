import sys

n = int(sys.stdin.readline())

while n > 0:
    sys.stdout.write('*' * n + '\n')
    n -= 1