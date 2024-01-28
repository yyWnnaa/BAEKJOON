import sys

# 입력받을 자연수의 개수 t
# 사실 이 코드에서 t는 안 쓰인다.
t = int(sys.stdin.readline())

# 완전수인지 검사하는 대상이 되는 자연수들의 리스트 n
n = [int(x) for x in input().split()]


for i in n:
    # 반복문 시작마다 sum값 초기화
    sum = 0 
    
    for j in range(1,i):
        if i % j == 0: # 약수이면
            sum += j   # sum에 더한다

    '''j = 1
    while j < i:
        if i % j ==0:
            sum += j

        j += 1'''     #while을 사용한 똑같은 반복문

    if sum == i: #완전수
        sys.stdout.write('Perfect\n')
    elif sum < i: #부족수
        sys.stdout.write('Deficient\n')
    elif sum > i: #과잉수
        sys.stdout.write('Abundant\n')