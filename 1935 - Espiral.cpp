#include <bits/stdc++.h>

typedef long long llint;

int main() {
  llint n, b, l, c, f, q, x;

  scanf("%lld %lld", &n, &b);

  if (b == n * n) {
    c = (n + 1) / 2;
    l = (n % 2) ? c: c + 1;
  }
  else {
    q = ceil((n - sqrtl(n * n - b)) / 2.0); //Calcula em que quadrado q está o b
    x = q - 1;
    b = b - 4 * x * (n - x);                //Calcula o total de casas usadas no quadrado q
    n = n - 2 * q + 2;                      //Largura do quadrado q
    f = (b - 1) / (n - 1);       

    b = b - f * (n - 1);    

    switch (f) {
      case 0: l = q;
              c = q + b - 1;
              break;
      case 1: l = q + b - 1;
              c = n + q - 1;
              break;
      case 2: l = n + q - 1;
              c = n + q - b;
              break;
      case 3: l = n + q - b;
              c = q;
    }
  }

  printf("%lld %lld\n", l, c);
  return 0;
}