import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    
    A2 = a*a
    B2 = b*b
    C2 = c*c
    
    if a ==  b == c == 0:
        break
    elif A2 == B2 + C2 or B2 == A2 + C2 or C2 == A2 + B2:
        sys.stdout.write('right')
        sys.stdout.write('\n')
    else:
        sys.stdout.write('wrong')
        sys.stdout.write('\n')