#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int N;
        cin >> N;
        cout << (1 << ((N + 1) / 2 + 1)) - N % 2 - 1 << endl;
    }
    return 0;
}