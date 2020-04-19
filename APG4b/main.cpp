#include <bits/stdc++.h>
using namespace std;
#define EX15 1
#if EX15
// 1人のテストの点数を表す配列から合計点を計算して返す関数
// 引数 scores: scores.at(i)にi番目のテストの点数が入っている
// 返り値: 1人のテストの合計点
int sum(vector<int> scores) {
    int x = 0;
    for(int i = 0 ; i < scores.size() ; i ++){
        x += scores.at(i);
    }
    return x;
}

// 3人の合計点からプレゼントの予算を計算して出力する関数
// 引数 sum_a: A君のテストの合計点
// 引数 sum_b: B君のテストの合計点
// 引数 sum_c: C君のテストの合計点
// 返り値: なし
void output(int sum_a, int sum_b, int sum_c) {
    cout << sum_a * sum_b * sum_c << endl;
}

// -------------------
// ここから先は変更しない
// -------------------

// N個の入力を受け取って配列に入れて返す関数
// 引数 N: 入力を受け取る個数
// 返り値: 受け取ったN個の入力の配列
vector<int> input(int N) {
    vector<int> vec(N);
    for (int i = 0; i < N; i++) {
        cin >> vec.at(i);
    }
    return vec;
}

int main() {
    // 科目の数Nを受け取る
    int N;
    cin >> N;

    // それぞれのテストの点数を受け取る
    vector<int> A = input(N);
    vector<int> B = input(N);
    vector<int> C = input(N);

    // それぞれの合計点を計算
    int sum_A = sum(A);
    int sum_B = sum(B);
    int sum_C = sum(C);

    // プレゼントの予算を出力
    output(sum_A, sum_B, sum_C);
}
#endif
#if EX14
int main(){
    int A, B, C;
    cin >> A >> B >> C;
    vector<int> vec = {A,B,C};
    sort(vec.begin(),vec.end());
    cout << vec.at(2) - vec.at(0) << endl;
}
#endif
#if EX13
int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    // a b c d e ... って空白区切りも取得できる
    for(int i = 0 ; i < N ; i++){
        cin >> A.at(i);
    }

    // 平均点の算出 (0は初期値)
    float ave = accumulate(A.begin(), A.end(),0) / N;

    // 離れている値の出力
    for(int i = 0 ; i < N ; i++ ){
        cout << abs(ave - A.at(i)) << endl;
    }
}
#endif
#if EX12
int main() {
    string S;
    cin >> S;
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
