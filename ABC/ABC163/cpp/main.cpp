#include <bits/stdc++.h>
using namespace std;
vector<int> InputLine(int N);

int main() {
    int n;
    cin >> n;
    vector<int> a = InputLine(n);

    cout << "hello" << endl;
}

vector<int> InputLine(int N) {
    vector<int> vec(N);
    for (int i = 0; i < N; i++) {
        cin >> vec.at(i);
    }
    return vec;
}
