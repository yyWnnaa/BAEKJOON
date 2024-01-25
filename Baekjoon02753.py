import sys

yy = int(sys.stdin.readline())

#4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
#(4의 배수 and 100의 배수가 아닐 때)or 400의 배수
if (yy % 4 == 0 and yy % 100 != 0) or yy % 400 == 0:
    sys.stdout.write(str(1))
else:
    sys.stdout.write(str(0))