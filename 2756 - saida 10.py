space = 7
space2 = 1
A = ['A', 'B', 'C', 'D', 'E']
max = 5

for i in range(0, max):
    if (i == 0):
        print((space*' ') + A[i])
        space -=1
    else:
        print(space*' ' + A[i] + (space2* ' ') + A[i])
        space -=1
        space2 += 2

space += 2  
space2 -= 4

for i in range(max-2, -1, -1):
    if (i == 0):
        print((space*' ') + A[i])
    else:
        print(space*' ' + A[i] + (space2* ' ') + A[i])
        space +=1
        space2 -= 2
    