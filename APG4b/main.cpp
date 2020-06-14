#include <bits/stdc++.h>
using namespace std;

#define vint vector<int>
#define vvint vector<vint>
#define sint stack<int>
#define qint queue<int>
#define rep(i, n) for(int i=0;i<(int)(n);i++) // 繰り返し処理
#define all(x) (x).begin(),(x).end() // 全体 こんな感じで使う→sort(all(a));
#define ct(a) cout << a << endl
#define iceil(a,b) (a+(b-1))/b //int ceil : 繰り上げの割り算 通常のceilではceil((7.0/2.0))のようにしなければならなかった。
#define ul unsigned long
vint CinLine(int N){vint v(N);for(int i=0;i<N;i++){cin >> v.at(i);}return v;}//cin line 連続でvectorに格納
void CoutLine(vint v){for(int i=0;i<v.size()-1;i++){cout<<v.at(i)<<" ";}cout << v.at(v.size()-1)<<endl;}
// str.substr(開始位置, 取り出す長さ);

void Main(){
    ul n;
    cin >> n;

    set<ul> seta;
    for(ul i = 0;i<n;i++){
        ul x;
        cin >> x;
        seta.insert(x);
    }
    vector<ul> a(seta.begin(), seta.end());

    if(a.size() == 1){
        ct(0);
        return;
    }

    vector<bool> isOK(n);
    for(ul i = 0;i<n;i++){
        isOK[i] = true;
    }

    for(ul i = 0 ; i < a.size() ; i++){
        for(ul j = 0 ; j < a.size() ; j++){
            if(i==j){
                break;
            }
            if(isOK[i]){//脱落していなければ
                if(a[i] % a[j] == 0){
                    //cout << a[i] << " " << a[j] << " " << a[i]%a[j]<< endl;
                    // 割り切れた
                    isOK[i] = false;
                    break;
                }
            }
        }
    }
    ul ans = 0;
    for(auto x : isOK){
        if(x == true){
            ans++;
        }
    }

    ct(ans);
}

int main() {
    Main();
}