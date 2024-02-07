import sys

s = int(sys.stdin.readline())

n = 0

while True:
    nMemory = n #초과시 1회의 반복 취소용

    n = n + 1
    nGgajiSum = (n * (n + 1) / 2) # 1부터 n까지의 합

    if nGgajiSum == s:
        break
    elif nGgajiSum > s:
        n = nMemory # 1회의 반복을 취소한다
        break

sys.stdout.write(str(n))

'''
1부터 더하다가 그 수가 같으면 n을 그냥 출력하면 되는거고
그 수가 s를 넘어가면 
예를들어서 s가 12인데  n까지합이 13이 되면
1회 취소해서
이전의 수들로 "만들수 있는 최소합" 10으로 돌아가서 (1+2+3+4) 
여기서 4만 6으로 바꾸면
1 2 3 6 이렇게 되는 코드
'''