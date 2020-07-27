#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

  char s1[61], s2[62], cpf[12];
  int i, j, ponto, p;

  scanf("%s %s", s1, s2);
  // CPF
  for (i = 0, j = 0; j < 11; i++)
    if (isdigit(s1[i]))
      cpf[j++] = s1[i];

  cpf[j] = '\0';

  // valor 1
  ponto = p = 0;
  for (j = 0; s1[i] && p < 3; i++)
    if (isdigit(s1[i]) || s1[i] == '.'){
      s1[j++] = s1[i] ;

      if (s1[i] == '.') ponto = 1;
      if (ponto) p++;

    }
  s1[j] = '\0';

  // valor 2
  ponto = p = 0;
  for (i = 0, j = 0; s2[i] && p < 3; i++)
    if (isdigit(s2[i]) || s2[i] == '.'){
      s2[j++] = s2[i];

      if (s2[i] == '.') ponto = 1;
      if (ponto) p++;
    }

  s2[j] = '\0';

  printf("cpf %s\n", cpf);
  printf("%.2lf\n", strtod(s1, NULL) + strtod(s2, NULL));

  return 0;
}