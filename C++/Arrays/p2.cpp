#include <iostream>
void createArray(int*& nums, int size) {
    // Allocate a new dynamic array
    nums = new int[size];
    // Fill it with 0, 10, 20, 30...
    for (int i = 0, j = 0; i < size; i++, j+=10){
        nums[i] = j;
}
}
void printArray( int nums[], int size){
    for ( int i = 0; i < size; ++i){
        std::cout << nums[i] << std::endl;
    }
}

int main() {
    int* nums = nullptr;
    int size = 5;

    createArray(nums, size);
    printArray(nums, size);

    delete[] nums;
}
