n = input().split('.')

if int(n[0]) == 0:
    n[0] = '0'

while n[1][0] == '0' and len(n[1]) > 1  :
    n[1] = n[1][1:]

print(n[1] + "." + n[0])