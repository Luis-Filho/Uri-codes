from itertools import permutations 

t = int(input())
case = 1

while t:
    t -= 1
    A = [int(i) for i in input().split()][1:]
    print(list(permutations(A)))

      
    
    
    #print("Case {}: {}".format(case, total_1))
    
    
    
    
    