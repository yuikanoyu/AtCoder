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
//#define ul unsigned long
vint CinLine(int N){vint v(N);for(int i=0;i<N;i++){cin >> v.at(i);}return v;}//cin line 連続でvectorに格納
void CoutLine(vint v){for(int i=0;i<v.size()-1;i++){cout<<v.at(i)<<" ";}cout << v.at(v.size()-1)<<endl;}
// str.substr(開始位置, 取り出す長さ);

void Main(){
    int n;
    cin >> n;
    int pt = 0;
    rep(i,n){
        int d,p;
        cin >> d >> p;

        switch(d){
            case 3:
            case 13:
            case 23:
            case 30:
            case 31:
                pt += p * 0.03f;
                break;
            case 5:
            case 15:
            case 25:
                pt += p * 0.05f;
                break;
            default:
                pt += p * 0.01f;
                break;
        }
    }
    ct(pt);
}

int main() {
    Main();
}