import sys
input = sys.stdin.readline

n, m = map(int, input().split())

m2738 = []

for _ in range(n):
    # m2738이라는 행렬에 첫번째 행렬을 받는다. 
    # 이 행렬에 두번째 행렬을 받자마자 더하면서 출력할것임
    m2738.append(list(map(int, input().split())))
    
for i in range(n):
    temp = list(map(int, input().split()))
    
    for j in range(m):
      # m2738[i][j] += temp[j]
      # 윗줄의 코드는 다음과 같음 :
      # m2738[i][j] = m2738[i][j] + temp[j]
      
      # sys.stdout.write(str(m2738[i][j]) +  " ")
      # 윗줄의 코드는 다음과 같음 :  
      # print(m2738[i][j] , end = " ")
        
      # 굳이 m2738에 저장하지 않고 바로 출력할수도 있다.
      # 17, 21라인을 합쳐서
        sys.stdout.write(str(m2738[i][j] + temp[j]) + ' ') 
      # 윗줄의 코드는 다음과 같음 : 
      # print(m2738[i][j] + temp[j], end = " ")
        
    sys.stdout.write('\n')
  # 윗줄의 코드는 다음과 같음 : 
  # print()