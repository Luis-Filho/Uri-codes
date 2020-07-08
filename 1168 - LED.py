A = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

n = int(input())


while n:
    total = 0
    n -= 1
    for i in input():
        total += (A[int(i)])

    print("{} leds".format(total))
