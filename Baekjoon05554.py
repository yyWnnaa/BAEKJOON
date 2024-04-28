import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

e = a+b+c+d
h = e // 60
s = e % 60

print(h)
print(s)