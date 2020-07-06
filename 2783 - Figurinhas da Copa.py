n, m, c = input().split(" ")

n = int(n)
m = int(m)
c = int(c)

A = input().split(" ")
B = input().split(" ")

for i in A:
    if i in B:
        m -= 1

print(m)