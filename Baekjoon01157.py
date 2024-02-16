import sys

a = input().upper()
#upper는 입력받은 문자를 대문자로 만들어준다
#upper의 반대로 모두 소문자로 받아주는건 lower()
#readline으로 입력받을 경우 뭔가 문제가 있다...

a_set = list(set(a))
#set은 중복되는거 제거
#ellemimi 입력시 elmi만 남음
#a_set은 오직 아래의 for문을 위한것임
#list는 나중에 index를 사용하기 위해

Acnt = []

for i in a_set:
    count = a.count
    Acnt.append(count(i))
    
if Acnt.count(max(Acnt)) > 1: #max값이 2 이상이면
    sys.stdout.write("?")
else:
    sys.stdout.write(str(a_set[Acnt.index(max(Acnt))]))
    #Acnt 중 count가 가장 많이 선언된 index의 위치를 반환하고
    #그 값을 Acnt[index]

'''
print()
print()

print("a : ", end='')    
print(a)

print("a_set : ", end='')  
print(a_set)

print("Acnt : ", end='')  
print(Acnt)

print("max(Acnt) : ", end='')  
print(max(Acnt))

print("Acnt.index(max(Acnt)) : ", end='')  
print(Acnt.index(max(Acnt)))

print("a_set[Acnt.index(max(Acnt))] : ", end='')  
print(a_set[Acnt.index(max(Acnt))])
'''