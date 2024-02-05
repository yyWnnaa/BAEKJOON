import sys

input1152 = sys.stdin.readline().split(' ')

lastIndex = len(input1152)-1

if input1152[0] == '' and input1152[lastIndex] == '\n':
    print(len(input1152)-2)
elif input1152[0] == '' or input1152[lastIndex] == '\n': 
    print(len(input1152)-1)
else:
    print(len(input1152))
