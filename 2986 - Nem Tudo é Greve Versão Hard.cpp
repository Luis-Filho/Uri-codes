#include <bits/stdc++.h>

using namespace std;

const int m = 1000000007;

int main() {
    int i, n, V[100001] = {0, 1, 2, 4};
    
    for (i = 4; i < 100001; i++)
        V[i] = (((V[i-1] + V[i-2]) % m) + V[i-3]) % m;

    cin >> n ;

    cout << V[n] << endl;



    return 0;
}
