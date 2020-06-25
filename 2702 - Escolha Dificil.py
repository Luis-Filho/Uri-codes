A = [int(i) for i in input().split(' ')]
B = [int(i) for i in input().split(' ')]

qtd = 0

if B[0] > A[0]:
    qtd += (B[0] - A[0])

if B[1] > A[1]:
    qtd += (B[1] - A[1])

if B[2] > A[2]:
    qtd += (B[2] - A[2])

print(qtd)