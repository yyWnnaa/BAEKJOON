import sys

n = int(sys.stdin.readline())

while True:
    sys.stdout.write(str(n))
    sys.stdout.write('\n')
    n -= 1
    if n == 0:
        break