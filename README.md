# BAEKJOON 10156
import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b, c = map(int, input().split())

res = a * b - c
if res < 0:
    res = 0
    
print(str(res))
