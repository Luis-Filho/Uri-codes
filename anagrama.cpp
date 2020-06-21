#include <iostream>

using namespace std;

bool anagrama(string a, string b);

int main(){
    string a, b;

    cin >> a;
    cin >> b;

    if (anagrama(a, b))
        cout << "São anagramas!\n";
    else 
        cout << "Não são anagramas!\n";

    return 0;
}

bool anagrama(string a, string b){
    int i;
    int vet[10];

    for (i = 0; i < 10; i++) vet[i] = 0;

    for (i = 0; a[i]; i++){
        vet[a[i] - '0']++;
        vet[b[i] - '0']--;
    }

    for (i = 0; i < 10; i++)
        if (vet[i] != 0)
            return false;

    return true;
}