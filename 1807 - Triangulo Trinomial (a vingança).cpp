#include <stdio.h>

#define llint long long int

llint pot (int a, int m);
llint c = 2147483647;

int main(){
  int a;

  scanf("%d", &a);

  printf("%lld\n", pot(3, a));

  return 0;
}

llint pot (int a, int m) {
  if (m == 0)
    return 1;
  else
    if (m == 1)
      return a;
    else {
      llint r = pot(a, m/2) % c;

      r = (r  * r) % c;

      if (m % 2)
        r = (r * a) % c;

      return r;
    }
}
