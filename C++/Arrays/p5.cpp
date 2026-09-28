#include <iostream>
using namespace std;

int* addressOfLargest(int nums[], int size){
    int* largest = &nums[0];

    for ( int i = 0; i < size  ; i++){
        if ( nums[i] > *largest) largest = &nums[i];
    }
    return largest;
}

int main(){
    int nums[] = {8, 20, 3, 17, 6};
    int* largest = addressOfLargest(nums, 5);
    if (largest != nullptr) {
        *largest = -1; 
    }
     for ( int i = 0; i < 5; i++){
        cout << nums[i] << "\t";
    }   
}

