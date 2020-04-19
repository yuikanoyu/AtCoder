#include <bits/stdc++.h>
using namespace std;
vector<int> InputLine(int N);

int main() {
    int ans = 0;
    int N;
    cin >> N;
    vector<int> A = InputLine(N);


}

vector<int> InputLine(int N) {
    vector<int> vec(N);
    for (int i = 0; i < N; i++) {
        cin >> vec.at(i);
    }
    return vec;
}

#if A
int main() {
    int R;
    cin >> R;
    cout << 2*R*3.14159265359 << endl;
}
#endif

#if B
int main() {
    int N,M;
    cin >> N >> M;
    vector<int> A = InputLine(M);
    int ans = N - accumulate(A.begin(),A.end(),0);
    if(ans < 0){
        ans = -1;
    }
    cout << ans << endl;
}
#endif

#if C
int main() {
    int N;
    cin >> N;
    vector<int> A = InputLine(N-1);
    vector<int> ans(N);

    for(int i = 0; i < A.size() ; i++){
        ans.at(A.at(i)-1)++;
    }

    for(int i = 0 ; i < ans.size() ; i++){
        cout << ans.at(i) << endl;
    }

}
#endif

#if D_NG
int main() {
    int ans = 0;
    int N , K;
    cin >> N >> K;
    int n = N+1;
    for(int k = K; k < n ; k++){
        vector<vector<long long int>> v(n+1,vector<long long int>(n+1,0));
        comb(v);
        ans += v[n][k];
        cout << v[n][k]<< endl;
    }
    cout << (ans+1)%1000000007 << endl;
}

void comb(vector<vector <long long int> > &v){
    for(int i = 0;i <v.size(); i++){
        v[i][0]=1;
        v[i][i]=1;
    }
    for(int k = 1;k <v.size();k++){
        for(int j = 1;j<k;j++){
            v[k][j]=(v[k-1][j-1]+v[k-1][j]);
        }
    }
}
#endif