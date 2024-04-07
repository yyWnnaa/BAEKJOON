import sys

n = int(sys.stdin.readline())
list10814 = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    list10814.append([int(age), name])
    #list10814.append((int(age), name))

list10814.sort(key = lambda x : x[0])
'''람다 표현식으로 간단하게 정리
중첩리스트 중 첫 번쩨(나이) 요소에 기준 값을 설정하여
이를 바탕으로 정렬하는 것 
참고한 블로그 : https://blog.naver.com/ceroopark/222625828351

def sort_by_age(x):
    return x[0]
sorted_list10814 = tuple(sorted(list10814, key = sort_by_age))
age 기준으로 정렬, 위의 lambda식과 동일
참고한 블로그 : https://blog.naver.com/dhtjdqls2/222658448803 '''

for j in range(n):
    sys.stdout.write(str(list10814[j][0]) + ' ' + str(list10814[j][1]) + '\n')
    #print(mergedList[i][0], mergedList[i][1])