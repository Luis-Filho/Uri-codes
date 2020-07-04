a, b = input().split(" ")
a = int(a)
b = int(b)

if b - a >= 3:
    print("Muito bem! Apresenta antes do Natal!")
elif a <= b and b - a < 3:
    print("Parece o trabalho do meu filho!")
    if a + 2 < 24:
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")
else:
    print("Eu odeio a professora!")
