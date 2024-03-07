import sys

t = int(sys.stdin.readline())

for i in range(t):
    asum = 0
    bsum = 0
    for j in range(9):
        a, b = map(int, sys.stdin.readline().split())
        asum += a
        bsum += b
    
    if asum > bsum:
        print("Yonsei")
    elif bsum > asum:
        print("Korea")
    elif asum == bsum:
        print("Draw")