import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

if a < b < c < d:
    sys.stdout.write('Fish Rising')
elif a > b > c > d:
    sys.stdout.write('Fish Diving')
elif a == b == c == d:
    sys.stdout.write('Fish At Constant Depth')
else:
    sys.stdout.write('No fish')