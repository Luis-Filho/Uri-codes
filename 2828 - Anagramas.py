resto = 1000000007

def fat (n):
    a = 1

    while n > 0:
        a = (a * n) % resto
        n -= 1

    return a

n = input()

# combinação
#numerador
c = fat(len(n))

lst_repeat = []
#denominador
d = 1

for i in n:
    qtd = n.count(i)
    if qtd > 1 and not(i in lst_repeat):        
        lst_repeat.append(i)        
        c = c * pow(fat(qtd), -1) * resto


print(c)
print(lst_repeat)