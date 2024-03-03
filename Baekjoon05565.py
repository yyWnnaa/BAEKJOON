import sys
print = sys.stdout.write

all = int(sys.stdin.readline())

for i in range(9):
    book = int(sys.stdin.readline())
    all -= book
    
print(str(all))