for k in range(1):
    try:
        n = int(input())
        a = []

        for i in range(n):
            a.append(int(input()))
    
        a.sort()

        for j in a:
            print(j)
            
    except:
        break