#include <bits/stdc++.h>

using namespace std;

int main() {

    int l, n;
    double a;
    
    cin >> n;

    while (n--){
        cin >> l;
        a = (5 * l * l) / (4 * tan(36 * M_PI / 180));
        cout << setprecision(3) << fixed << a << endl;
    }
    
    return 0;
}