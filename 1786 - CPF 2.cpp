#include <stdio.h>

int main(){

  int i, total, j, d1[11];
  char d[15];

  while(scanf("%s", d) != EOF){
    for(i = 0; d[i] ; i++)
      d1[i] = d[i] - '0';
    total = 0;
    for(i = 0; i < 9; i++)
      total += d1[i] * (i+1);

    d1[9] = ((total % 11 == 10) ? 0 : total % 11);

    total = 0;
    for(i = 0; i < 9; i++)
      total += d1[i] * (9 - i);

    d1[10] = ((total % 11 == 10) ? 0 : total % 11);

    for(i = 0; i < 11; i++){
      if(i == 3 || i == 6)
        printf(".");

      if(i == 9)
        printf("-");

      printf("%d", d1[i]);
    }

    printf("\n");

  }

  return 0;
}
