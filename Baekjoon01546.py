n = int(input())
a = [int(x) for x in input().split()]

a.sort()   # 최댓값을 구하기 위해 정렬
m = a[n-1] # 정렬 후 리스트의 마지막 값이 최댓값

sum = 0.0
# sum을 실수형으로 정의
# 다른 좋은 방법이 있을 것 같음

for i in a:
    new_a = i/m*100
    sum += new_a
# '모든' 점수를 고치는 것,
# 매 반복마다 합을 저장    

print(sum/n)
#평균을 출력