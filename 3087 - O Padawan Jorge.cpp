#include <bits/stdc++.h>

int S[50] = {1};

int main (){
    int i, n, s, c, l, q, x, p;

    for (i = 1; i < 50; i++)
        S[i] = i * 8;

    scanf("%d %d", &n, &s);
    
    if (s == n*n){
        l = 0;
        c = n-1;
    } else {
        q = 0;
        for (i = 0; s >= S[i]; i++, q++)
            s -= S[i];

        if (s == 0) {
            l = n / 2 - q;
            c = n / 2 + q - 1;
        } else {
            x = (s - 1) / (2 * q);
            p = (s - 1) % (2 * q);

            printf("%d %d", x, p);
            /*Calcular linha e coluna, dependendo do segmento*/
        }
      
    }

    return 0;
}