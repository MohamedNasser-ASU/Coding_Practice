#include <iostream>
using namespace std;

int* findValue(int nums[], int size, int target){
    
    int* result = nullptr;
    for ( int i = 0; i < size; i++)
    {
        if ( target == nums[i] )
        {
            result = &nums[i];
            return result;
        }

    }

    return result;
    
}

int main(){
    int nums[] = {7, 4, 9, 4, 2};
    int* result = findValue(nums, 5, 4);
    if (result != nullptr) {
        *result = 100; 
    }
    // Expected array: 7 100 9 4 2
    for ( int i = 0; i < 5; i++){
        cout << nums[i] << "\t";
    }
}

