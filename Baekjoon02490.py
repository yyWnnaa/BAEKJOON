for i in range(3):
    a = [int(x) for x in input().split()]
    a.sort()
    if a[3] == 0:
        print('D')
    elif a[2] == 0:
        print('C')
    elif a[1] == 0:
        print('B')
    elif a[0] == 0:
        print('A')
    elif a[0] == 1:
        print('E')