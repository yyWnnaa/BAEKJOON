import sys

n1, n2, n3 = map(int, sys.stdin.readline().split())
ss = sys.stdin.readline().rstrip()

a=0
b=0
c=0

if n1 < n2 < n3:
    a = n1
    b = n2 
    c = n3
elif n1 < n3 < n2:
    a = n1
    b = n3
    c = n2
elif n2 < n1 < n3:
    a = n2
    b = n1
    c = n3
elif n2 < n3 < n1:
    a = n2
    b = n3
    c = n1
elif n3 < n1 < n2:
    a = n3
    b = n1
    c = n2
elif n3 < n2 < n1:
    a = n3
    b = n2
    c = n1

if ss[0] == 'A':
    sys.stdout.write(str(a) + ' ')
elif ss[0] == 'B':
    sys.stdout.write(str(b) + ' ')
elif ss[0] == 'C':
    sys.stdout.write(str(c) + ' ')

if ss[1] == 'A':
    sys.stdout.write(str(a) + ' ')
elif ss[1] == 'B':
    sys.stdout.write(str(b) + ' ')
elif ss[1] == 'C':
    sys.stdout.write(str(c) + ' ')

if ss[2] == 'A':
    sys.stdout.write(str(a))
elif ss[2] == 'B':
    sys.stdout.write(str(b))
elif ss[2] == 'C':
    sys.stdout.write(str(c))