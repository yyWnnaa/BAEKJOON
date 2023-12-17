import sys

a = [int(x) for x in sys.stdin.readline().split()]

n = a[0]
m = a[1]

if m == 1 or m == 2:
    print("NEWBIE!")
elif m <= n:
    print("OLDBIE!")
else:
    print("TLE!")