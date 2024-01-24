import sys
mm = int(sys.stdin.readline())
dd = int(sys.stdin.readline())

if mm == 2:
    if dd == 18:
        sys.stdout.write('Sepcial')
    elif dd < 18:
        sys.stdout.write('Before')
    elif dd > 18:
        sys.stdout.write('After')
elif mm < 2:
    sys.stdout.write('Before')
elif mm > 2:
    sys.stdout.write('After')
