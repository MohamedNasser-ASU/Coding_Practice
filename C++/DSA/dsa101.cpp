#include <cstddef>
#include <exception>
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};


int main(){

    struct Node third = {30, nullptr};
    struct Node second = {20, &third};
    struct Node first = {10, &second};

    Node* head = &first;
    Node* current = head;

    // while ( current != nullptr){
    //     cout << current->data << endl;
    //     current = current->next;
    // }
    
    // // sum of nodes
    // int sum = 0;
    // while (current != nullptr){
    //     sum += current->data;
    //     current = current->next;
    // }
    // cout << sum;
    
    // int target;
    // bool found = false;
    // cin >> target;
    // while ( current != nullptr){
    //     if (target == current->data){
    //         found = true;
    //         break;
    //     }
    //     current = current->next; 
    // }
    // if ( found ) cout << "Found" << endl;
    // else cout << "Not found" << endl;
    
    Node newNode {5, nullptr};
    
    newNode.next = &first;
    head = &newNode;
    
    Node lastNode {40, nullptr};


    while ( current->next != nullptr){
        current = current->next;
        }
    current->next = &lastNode;

    return 0;
}
//meow
