#include <iostream>
using namespace std;

void printMemory(const int nums[], int size){

    for(int i = 0; i < size; i++)
    {
        cout << i << "\t" << nums[i] << "\t" << *(nums+i) << "\t" << &nums[i] << "\t" << nums + i << "\t" << endl; 
    }
}

int main(){
    int nums[5] = {11, 22, 33, 44, 55};
    printMemory(nums, 5);

}

