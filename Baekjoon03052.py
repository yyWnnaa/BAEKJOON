import sys

a = []

for i in range(10): # 10번의 반복
    # 1.새로운 수를 입력받아 2.나머지를 구하고 3.리스트에 저장한다

    # 1. 새로운 수를 입력받아
    k = int(sys.stdin.readline())
    
    # 2. 나머지를 구하고
    newk = k % 42  
    
    # 3. 리스트에 저장한다
    a.append(newk)

a.sort() #비교를 위해 리스트를 정렬한다
DifferentCount = 10
beforej = 43  # 42의 나머지일수 없는 수 (중복 방지)

for j in a:
    if j == beforej:
        DifferentCount -= 1
    beforej = j  
#리스트에서 반복문을 돌리며 이전의 수와 같으면 카운트가 하나씩 차감
# 서로 다른 나머지가 몇 개인지 찾는 것이므로 같으면 차감시키는 것이다
sys.stdout.write(str(DifferentCount))
