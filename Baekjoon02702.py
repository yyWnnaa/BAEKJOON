import sys

t = int(sys.stdin.readline())
# 테스트 케이스의 개수 t

gcd_boj2702 = 1
# GCD Greatest Common Divisor 최대공약수

# LCM Least Common Multiple 최소공배수

for i in range(t):

    gcd_boj2702 = 1
    a, b = map(int, sys.stdin.readline().split())

    if a == b:
        gcd_boj2702 = a
        # a와 b가 같으면 gcd도 lcm도 모두 같음
    elif a>b:
        j = 9999
        while j >= 2:
            j = b
            if (a % j == 0) and (b % j == 0):
                gcd = j
                break
            j -= 1
    elif a<b:
        k = 9999
        while k >= 2:
            k = a
            if (a % k == 0) and (b % k == 0):
                gcd = k
                break
            k -= 1

    # a * b = gcd * lcm

    sys.stdout.write(str(a * b * gcd_boj2702))
    sys.stdout.write(" ")
    sys.stdout.write(str(gcd_boj2702))
    sys.stdout.write("\n")