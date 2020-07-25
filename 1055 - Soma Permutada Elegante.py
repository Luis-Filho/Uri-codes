t = int(input())
case = 1
while t:
    t -= 1
    A = sorted([int(i) for i in input().split()][1:])

    mid_list = (len(A) //2)  

    min_A = A[:mid_list] 
    max_A = A[mid_list:]

    i = len(min_A) -1
    j = len(max_A) -1
    B = []
    C = []
    
    while i >= 0 or j >= 0:
        if  i >= 0:
            B.append(min_A[i])
            i -= 1

        if  j >= 0:
            B.append(max_A[j])
            j -= 1


    j = len(max_A) -1
    i = 0
    while j >= 0 or i < len(min_A):
        if  j >= 0:
            C.append(max_A[j])
            j -= 1

        if  i < len(min_A):
            C.append(min_A[i])
            i += 1     

    total_1 = total_2 = 0

    for i in range(1, len(B)):
        total_1 += abs(B[i] - B[i-1])

    for i in range(1, len(C)):
        total_2 += abs(C[i] - C[i-1])
    
    
    #print(mid_list)
    print(A)
    #print(min_A)
    #print(max_A)
    print(B)
    print(C)
    print("Case {}: {}".format(case, total_1))
    print("Case {}: {}".format(case, total_2))
    case += 1
    
    
    