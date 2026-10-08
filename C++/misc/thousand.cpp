#include <iostream>
#include <ostream>
using namespace std;

int main(){

    cout << "Enter a number\n" << endl ;
    int num;
    cin >> num;
    int something;
    if ( num >= 1000){
        something = num % 1000;
        num /= 1000;
        
        cout << num << "," << something << endl;

    } else cout << num << endl;



}

