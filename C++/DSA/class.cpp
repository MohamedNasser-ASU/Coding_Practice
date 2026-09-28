#include <iostream>
#include <new>
using namespace std;

#define SIZE 50

class Rectangle {
private:
    double len, wid;
public:

    Rectangle() { len = 0; wid = 0;}
    Rectangle(double len, double wid) { this -> len = len; this -> wid = wid; }
     
    double getArea() { return this-> len * this -> wid; }
    
};
int main(){

    Rectangle *recs = new Rectangle[SIZE];
    recs[0] = Rectangle(5,3);
    cout << recs[0].getArea() << endl;
    delete[] recs;
}
