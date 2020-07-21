#include <stdio.h>
#include <math.h>

int bmq (int n);

int main() {
  int n;

  while (scanf("%d", &n) != EOF)
    printf("she loves %s\n", bmq(n)? "me" : "not"); 
  
  return 0;
}


int bmq (int n) {
    if (n == 0) return 0;

    if (n % 2) return !bmq(n/2);
    else return bmq(n/2);
}