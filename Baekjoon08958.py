t = int(input()) # 테스트 케이스의 개수

for i in range(t):  # t번만큼 반복문 수행
    
    input8958 = list(input()) #리스트로 입력을 받는다
    
    Ocount = 0    # O 가중치
    sum = 0       # 출력할 점수
    # 아래에서 사용된 Ocount와 sum값을 초기화해준다
    '''맨 아래에서 print 후에 0으로 초기화해줄수도 있으나,
    그러면 그 전에 한번 더 정의를 해줘야 해서 귀찮아진다 (코드a 참고)'''
    
    for j in input8958: #반복문에서 리스트의 요소 하나하나를 비교한다
        
        if j == 'O':
            Ocount += 1
        else:
            Ocount = 0
            
        sum += Ocount # X일때는 0점을 더해주는 것
           
    print(sum)    