a = list(input())

result = len(a)

if len(a) == 2:
    for i in range(len(a)-1):
        if a[i] == 'c' and a[i+1] == '-':
            result -= 1
        elif a[i] == 'c' and a[i+1] == '=':
            result -= 1
        elif a[i] == 'd' and a[i+1] == '-':
            result -= 1
        elif a[i] == 'l' and a[i+1] == 'j':
            result -= 1
        elif a[i] == 'n' and a[i+1] == 'j':
            result -= 1
        elif a[i] == 's' and a[i+1] == '=':
            result -= 1
        elif a[i] == 'z' and a[i+1] == '=':
            result -= 1


if len(a) >= 3:
    for i in range(len(a)-2):
        if a[i] == 'd' and a[i+1] == 'z' and a[i+2] == '=':
            result -= 1
            
    for i in range(len(a)-1):
        if a[i] == 'c' and a[i+1] == '-':
            result -= 1
        elif a[i] == 'c' and a[i+1] == '=':
            result -= 1
        elif a[i] == 'd' and a[i+1] == '-':
            result -= 1
        elif a[i] == 'l' and a[i+1] == 'j':
            result -= 1
        elif a[i] == 'n' and a[i+1] == 'j':
            result -= 1
        elif a[i] == 's' and a[i+1] == '=':
            result -= 1
        elif a[i] == 'z' and a[i+1] == '=':
            result -= 1
        
print(result)