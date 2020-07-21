#include <stdio.h>

int vergonha(int n,int k) {
  if(n == 1)
    return 1;
  else
    return (k-1 + vergonha(n-1,k)) %n + 1;
}

int main() {

    int NC,I, N, K;
    int L,J,TOTAL;

    scanf("%d",&NC);

    for(I=1; I <= NC ; I++){
        scanf("%d %d",&N,&K);

        printf("Case %d: %d\n",I, vergonha(N, K));
    }

    return 0;
}
