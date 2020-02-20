#include <bits/stdc++.h>
using namespace std;
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