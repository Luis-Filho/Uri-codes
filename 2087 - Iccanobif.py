n = int(input())
A = [1, 1]

for i in range(1, n):
    A.append(A[i-1] + A[i])

for i in range(n-1, -1, -1):
    if (i == 0):
        print(A[i])
    else :
        print("{} ".format(A[i]), end="")

