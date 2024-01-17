import sys
h, m = map(int, sys.stdin.readline().split())

if m >= 45:
    # m이 45보다 크다면 h는 그대로 출력하고
    # m에서만 45를 빼주면 된다.
    sys.stdout.write(str(h))
    sys.stdout.write(' ')
    sys.stdout.write(str(m-45))
elif m <= 44:
    # m이 44보다 작다면 시간까지 조작을 해주어야 한다.
    if h == 0:
        sys.stdout.write(str(23))
        # 0시 전은 23시
        sys.stdout.write(' ')
        sys.stdout.write(str(m+15)) 
        # m + 15 = 60 + m - 45
    else:
        sys.stdout.write(str(h-1))
        sys.stdout.write(' ')
        sys.stdout.write(str(m+15))
