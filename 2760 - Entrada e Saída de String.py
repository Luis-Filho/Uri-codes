a = input()
b = input()
c = input()
A = [a, b, c]
print("{}{}{}".format(a, b, c))
print("{}{}{}".format(b, c, a))
print("{}{}{}".format(c, a, b))

for i in A:
    if len(i) > 10:
        print("{}".format(i[:10]),end="")
    else:
        print("{}".format(i),end="")
print("")
