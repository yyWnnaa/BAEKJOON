import sys
a = int(sys.stdin.readline())

if 100 >= a and a >= 90:
    sys.stdout.write("A")
elif a >= 80:
    sys.stdout.write("B")
elif a >= 70:
    sys.stdout.write("C")
elif a >= 60:
    sys.stdout.write("D")
else:
    sys.stdout.write("F")