#include <stdio.h>
#include <math.h>

using namespace std;

int main(){
  long long x, y;
  int i, j, *p, d = 0;

  scanf("%lld", &x);
  y = (long long) pow(x, 0.5);

  if (x % 2 == 0){
    d++;
    x /= 2;
    while (x % 2 == 0)
      x /= 2;
  }

  for (i = 3; i <= y; i += 2)
    if (x % i == 0) {
      d++;
      x /= i;

      while (x % i == 0)
        x /= i;
    }

  if (x > 1)
    d++;

  printf("%d\n", (int) pow(2, d) - d - 1);
  return 0;
}
