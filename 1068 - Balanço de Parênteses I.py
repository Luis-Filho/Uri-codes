while True:
    try:
        A = []
        for i in input():
            if i == '(' or i == ')':
                if len(A) != 0 and i == ')' and A[-1] == '(':
                    A.pop()
                else:
                    A.append(i)

        if len(A) == 0:
            print("correct")
        else :
            print("incorrect")
                    
            
            
    except EOFError as e:
        break