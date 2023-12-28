import sys

n = int(sys.stdin.readline())
n2 = n - 1

m = 1
m2 = m 

#윗부분(중앙 라인 미포함)
while n: # n>0 이 TRUE
    #왼쪽
    sys.stdout.write('*' * m)

    #가운데 공백
    sys.stdout.write(' ' * (n-1))
    
    #맨 처음 반복문 실행에서, n이 5면 nn은 4
    #n이 1이면 nn은 0
    nn = n-1 
    sys.stdout.write(' ' * nn)

    #오른쪽
    sys.stdout.write('*' * m)
    
    sys.stdout.write('\n')

    n -= 1
    m += 1

#중앙 라인
ng = n * 2    
sys.stdout.write('*' * ng)

#아래부분 (중앙 라인 미포함)
while n2:
    #중간 아래로 왼쪽 출력
    sys.stdout.write('*' * n2)

    #중간 출력
    m4 = m2*2
    sys.stdout.write(' ' * m4)

    #중간 아래로 오른쪽 출력
    sys.stdout.write('*' * n2 + '\n')
    
    n2 -= 1
    m2 += 1
