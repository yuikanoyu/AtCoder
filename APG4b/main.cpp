#include <bits/stdc++.h>
using namespace std;
#define EX13 1
#if EX13
int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    int S = 0;
    int AV = 0;
    for(int i = 0; i<N; i++){
        cin >> A.at(i);
        S += A.at(i);
    }
    AV = S / N;
    for(int i = 0; i<N; i++){
        cout << abs( AV - A.at(i)) << endl;
    }
}
#endif
#if EX12
int main() {
    string S;
    cin >> S;

    // ここにプログラムを追記
    int length = S.size();
    int ans = 1;
    for(int i = 0; i< length;i++){
        switch(S.at(i)){
            case '+':
                ans++;
                break;
            case '-':
                ans--;
                break;
            default:
                break;
        }
    }
    cout << ans << endl;
}
#endif
#if EX11
int main() {
    int N, A;
    cin >> N >> A;
    for(int i = 1 ; i <= N; i++){
        string op;
        int B;
        cin >> op >> B;
        if( op == "+"){
            cout << i << ":";
            A += B;
            cout << A << endl;
        }else if(op == "-"){
            cout << i << ":";
            A -= B;
            cout << A << endl;
        }else if(op == "*"){
            cout << i << ":";
            A *= B;
            cout << A << endl;
        }else if(op == "/"){
            if(B != 0){
                cout << i << ":";
                A /= B;
                cout << A << endl;
            }else{
                cout << "error" << endl;
                break;
            }
        }else{
            cout << "error" << endl;
            break;
        }
    }
}
#endif
#if EX10
int main(){
    int A, B;
    cin >> A >> B;

    // ここにプログラムを追記
    int i;
    i = A;

    cout << "A:";
    while(i > 0){
        cout << "]";
        i--;
    }
    cout << endl;
    i = B;
    cout << "B:";
    while(i > 0){
        cout << "]";
        i--;
    }
    cout << endl;
}
#endif
#if EX9
int main(){
    int x, a, b;
    cin >> x >> a >> b;

    // 1.の出力
    x++;
    cout << x << endl;

    // ここにプログラムを追記
    // 2
    x *= (a + b);
    cout << x << endl;
    // 3
    x *= x;
    cout << x << endl;
    // 4
    x--;
    cout << x << endl;
}
#endif
#if EX8
int main() {
    int p;
    int price;
    string text;
    cin >> p;

    // パターン1
    if (p == 1) {
        cin >> price;
    }

    // パターン2
    if (p == 2) {
        cin >> text >> price;
        cout << text << "!" << endl;
    }

    int N;
    cin >> N;

    cout << price * N << endl;
}
#endif
#if EX7
int main() {
    // 変数a,b,cにtrueまたはfalseを代入してAtCoderと出力されるようにする。
    bool a = true;// true または false
    bool b = false;// true または false
    bool c = true;// true または false

    // ここから先は変更しないこと

    if (a) {
        cout << "At";
    }
    else {
        cout << "Yo";
    }

    if (!a && b) {
        cout << "Bo";
    }
    else if (!b || c) {
        cout << "Co";
    }

    if (a && b && c) {
        cout << "foo!";
    }
    else if (true && false) {
        cout << "yeah!";
    }
    else if (!a || c) {
        cout << "der";
    }

    cout << endl;
}
#endif
#if EX5
int main(){
    int A, B;
    string op;
    cin >> A >> op >> B;
    if( op == "+"){
        cout << A + B << endl;
    }else if(op == "-"){
        cout << A - B << endl;
    }else if(op == "*"){
        cout << A * B << endl;
    }else if(op == "/"){
        if(B != 0){
            cout << A / B << endl;
        }else{
            cout << "error" << endl;
        }
    }else{
        cout << "error" << endl;
    }
}
#endif
#if EX5
int main(){
    int A, B;
    cin >> A >> B;
    cout << A + B << endl;
}
#endif
#if EX4
int main(){
    // 一年の秒数
    int seconds = 365 * 24 * 60 * 60;

    // 以下のコメント/* */を消して追記する
    cout << 1 * seconds << endl;
    cout << 2 * seconds << endl;
    cout << 5 * seconds << endl;
    cout << 10 * seconds << endl;
}
#endif
#if EX3
int main(){
    cout << 100*(100+1)/2 << endl;
}
#endif

#if EX2
int main() {
    cout << "いつも" << 2525 << endl;
    cout << "AtCoderくん" << endl;
}
#endif