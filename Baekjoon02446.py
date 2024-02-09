import sys

n = int(sys.stdin.readline())
n3 = n
m = 1
m2 = m -1


while n3>1:
    # 왼쪽 출력
    sys.stdout.write(' ' * m2)
    sys.stdout.write('*' * n3)
    
    # 오른쪽 출력
    k2 = n3 -1
    sys.stdout.write('*' * k2 + '\n')
    
    n3 -= 1
    m2 += 1


while n: # n>0 이 TRUE
    nn = n-1 
    #맨 처음 반복문 실행에서, n이 5면 nn은 4
    #n이 1이면 nn은 0
    sys.stdout.write(' ' * nn)
    sys.stdout.write('*' * m)
    
    #오른쪽 출력
    j = m - 1
    sys.stdout.write('*' * j + '\n')
    
    n -= 1
    m += 1