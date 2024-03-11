import sys

n = int(sys.stdin.readline())

cnt0 = 0
cnt1 = 0

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        cnt0 += 1
    elif a == 1:
        cnt1 += 1

if cnt0 > cnt1:
    sys.stdout.write('Junhee is not cute!')
else:
    sys.stdout.write('Junhee is cute!')