n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(a[0], a[n-1])
