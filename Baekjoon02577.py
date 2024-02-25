import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

d = list(map(int, str(a * b * c)))
            
for i in range(len(d)):
    if d[i] == 0:
        count0 += 1
    elif d[i] == 1:
        count1 += 1
    elif d[i] == 2:
        count2 += 1
    elif d[i] == 3:
        count3 += 1
    elif d[i] == 4:
        count4 += 1
    elif d[i] == 5:
        count5 += 1
    elif d[i] == 6:
        count6 += 1
    elif d[i] == 7:
        count7 += 1
    elif d[i] == 8:
        count8 += 1
    elif d[i] == 9:
        count9 += 1    
        
print(count0)            
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
print(count6)
print(count7)
print(count8)
print(count9)