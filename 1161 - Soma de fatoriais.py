while True:

    try:
        a, b = input().split(" ")
        a = int(a)
        b = int(b)
        

        z = 1
        w = 1

        while a > 0 or b > 0:
            if a > 0:
                z *= a
                a -= 1
            
            if b > 0:
                w *= b
                b -= 1
            
        print(z + w)
    except EOFError as e:
        break