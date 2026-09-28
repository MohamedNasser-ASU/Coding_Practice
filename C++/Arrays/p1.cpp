#include <iostream>
using namespace std;

void addOne(int nums[], int size) {
    // Add 1 to every element
    for ( int i = 0; i < size; i++) nums[i]++;
}

int main() {
    int nums[4] = {2, 5, 7, 10};

    addOne(nums, 4);
    
    for (int i = 0; i<4; i++) cout << nums[i] << endl;

}
