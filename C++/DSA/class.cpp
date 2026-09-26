#include <iostream>
using namespace std;

#define SIZE 50

class Rectangle {
private:
    double len, wid;
public:

    Rectangle() { len = 0; wid = 0;}
    Rectangle(double len, double wid) { this -> len = len; this -> wid = wid; }
     
    double getArea( double len, double wid) { return len*wid; }
    
};
int main(){

    Rectangle rectangles[50];
    Rectangle *recs = new Rectangle[SIZE];
    delete[] recs;
}
