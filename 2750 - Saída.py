print("-" * 39)
print("|  decimal  |  octal  |  Hexadecimal  |")
print("-" * 39)

for i in range(0, 16):
    o = oct(i).replace('0o', '')
    h = hex(i).replace('0x', '')
    a = str(i)

    if (i < 10):
        a =' ' + a

    if i < 8:
        o = ' ' +o

    if i > 9:
        h = h.upper()
    print("|     {}    |   {}    |       {}       |".format(a, o, h))

print("-" * 39)