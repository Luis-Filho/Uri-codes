n = int(input())

print('E' if (n == 0) else 
      'D' if (n <= 35) else
      'C' if (n <= 60) else
      'B' if (n <= 85) else 
      'A')