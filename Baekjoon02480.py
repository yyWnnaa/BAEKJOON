import sys

a, b, c = map(int, sys.stdin.readline().split())

# 1. 같은 눈이 3개가 나오는 경우
if a == b and b == c: 
    money = 10000 + a * 1000
#=======================================================
# 2. 같은 눈이 2개만 나오는 경우 (각 3가지)
# 2-1. 첫번째 주사위의 눈과 두번째 주사위의 눈이 같은 경우
elif a == b and b != c: 
    money = 1000 + a * 100
# 2-2. 첫번째 주사위의 눈과 세번째 주사위의 눈이 같은 경우
elif a == c and b != c:
    money = 1000 + a * 100
# 2-3. 두번째 주사위의 눈과 세번째 주사위의 눈이 같은 경우
elif b == c and b != a:
    money = 1000 + b * 100
#=======================================================
# 3. 모두 다른 눈이 나오는 경우 (각 3가지)
else:
#elif a != b and b != c:
#elif a != b and b != c and a != c:
    # 첫번째 주사위의 눈이 가장 큰 경우
    if a > b and a > c:
        money = a * 100
    # 두번째 주사위의 눈이 가장 큰 경우
    elif b > a and b > c:
        money = b * 100
    # 세번째 주사위의 눈이 가장 큰 경우
    elif c > a and c > b:
        money = c * 100
        
sys.stdout.write(str(money))