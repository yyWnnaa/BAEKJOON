import sys

a, b = map(int, sys.stdin.readline().split())

# 하나하나 쪼갠다. a에 734를 입력할 경우 [7, 3, 4]가 된다.
a = list(map(int, str(a)))
b = list(map(int, str(b)))


def func_2908(c):
    # 반대로 출력할 것이므로 reverse 함수를 사용한 다음
    c.reverse()
    # 하나하나 출력하면 된다.
    for i in c:
        sys.stdout.write(str(i))

if a[2] > b[2]:
    func_2908(a)
elif a[2] < b[2]:
    func_2908(b)
elif a[1] > b[1]:
    func_2908(a)
elif a[1] < b[1]:
    func_2908(b)
elif a[0] > b[0]:
    func_2908(a)
elif a[0] < b[0]:
    func_2908(b)