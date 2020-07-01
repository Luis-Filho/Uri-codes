a = str(int(input()))
b = str(int(input()))
c = str(int(input()))

print("A = {}, B = {}, C = {}".format(a, b, c))
x = ((10 - len(a))* " ") + a
y = ((10 - len(b))* " ") + b
z = ((10 - len(c))* " ") + c

print("A = {}, B = {}, C = {}".format(x, y, z))

if int(a) < 0:
    x = "-" + ((10 - len(a))* "0") + a[1:]
else:
    x = ((10 - len(a))* "0") + a

if int(b) < 0:
    y = "-" + ((10 - len(b))* "0") + b[1:]
else:
    y = ((10 - len(b))* "0") + b

if int(c) < 0:
    z = "-" + ((10 - len(c))* "0") + c[1:]
else:
    z = ((10 - len(c))* "0") + c

print("A = {}, B = {}, C = {}".format(x, y, z))

x = a+ ((10 - len(a))* " ")
y = b +((10 - len(b))* " ")
z = c + ((10 - len(c))* " ")

print("A = {}, B = {}, C = {}".format(x, y, z))