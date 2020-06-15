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
    int L;
    int u,a,b;
    int v;
    cin >> L;
    cin >> u >> a >> b;
    cin >> v;

    int vt = L * v;

    int ut = 0;
    int ul = 0;
    int dis = 0;
    while(true){

        ul++;
        ut += u;

        if(ul >= L){
            break;
        }

        dis++;
        if(dis >= a){
            dis = 0;
            ut+= b;
        }
    }
    //cout << vt << " " << ut << endl ;
    if(ut < vt){
        ct("USAGI");
    }else if(vt < ut){
        ct("KAME");
    }else{
        ct("DRAW");
    }
}

int main() {
    Main();
}