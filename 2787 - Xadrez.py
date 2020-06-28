l = int(input())
c = int(input())

if (l%2 == 1 and c % 2 == 1) or (l%2 == 0 and c%2 == 0): 
    print(1)
else:
    print(0)