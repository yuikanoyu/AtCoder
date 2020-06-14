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
vint CinLine(int N){vint v(N);for(int i=0;i<N;i++){cin >> v.at(i);}return v;}//cin line 連続でvectorに格納
void CoutLine(vint v){for(int i=0;i<v.size()-1;i++){cout<<v.at(i)<<" ";}cout << v.at(v.size()-1)<<endl;}
// str.substr(開始位置, 取り出す長さ);

int vector_finder(std::vector<int> vec, int number) {
    auto itr = std::find(vec.begin(), vec.end(), number);
    size_t index = std::distance( vec.begin(), itr );
    if (index != vec.size()) { // 発見できたとき
        return 1;
    }
    else { // 発見できなかったとき
        return 0;
    }
}

int main() {
    int x,n;
    cin >> x >> n;
    vint p(n);
    p = CinLine(n);
    int ans = x;
    int i = 0;
    bool isPlus = true;
    while(true){
        if(isPlus) ans += i;
        else  ans -= i;
        //ct(ans);
        if(vector_finder(p,ans) == 0){
            break;
        }
        i++;
        if(isPlus) isPlus = false;
        else isPlus = true;
    }
    ct(ans);

}