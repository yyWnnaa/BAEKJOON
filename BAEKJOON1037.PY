n = int(input())
a = [int(x) for x in input().split()]

a.sort()

min = a[0]
max = a[n-1]

print(max*min)