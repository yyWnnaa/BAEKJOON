import sys

n = int(sys.stdin.readline())
m =0

while n > 0:
    sys.stdout.write(' ' * m)
    sys.stdout.write('*' * n + '\n')
    m += 1
    n -= 1