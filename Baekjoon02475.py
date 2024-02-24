import sys

a = [int(x) for x in sys.stdin.readline().split()]

sum = 0

for i in a:
    sum += i*i

sys.stdout.write(str(sum%10))