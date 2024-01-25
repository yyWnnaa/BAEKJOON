import sys
n = int(sys.stdin.readline())

n5 = n * 5

for i in range(n5 -1):
    print('@' * n)

for j in range(n):
    sys.stdout.write('@' * n5 + '\n')