import sys
t = int(sys.stdin.readline())
 
# 5618번에서 사용한 함수
# 두 수의 공약수는 두 수의 최대공약수의 약수
def gcd(a, b): #최대공약수를 구하는 함수 (재귀함수)
    if a == 0:
        return b #재귀함수가 종료되는 조건은 return b가 될 때 까지
    return gcd(b % a, a)
 
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    gcd1934 = gcd(a, b)
    # GCD * LCM = a * b   정수론입문 내용
    # 따라서 LCM = a * b / GCD
    lcm1934 = a * b // gcd1934
    sys.stdout.write(str(lcm1934) + '\n')