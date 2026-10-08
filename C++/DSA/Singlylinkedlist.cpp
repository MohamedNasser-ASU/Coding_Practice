#include <cstddef>
#include <iostream>
using namespace std;


struct Node{
    int id;
    Node* nextNode;
};

// prototypes
void add    (int id, Node* head);
void remove (int id, Node*& head);
void search (int id, Node* head);
void display(Node* head);
void insert (int id, Node*& head, int position);


int main(){

    cout << "Student Registration System" << endl;
    Node* head = nullptr;

    int id, position;
    char choice;
        
   
    while (1){

        if ( head == nullptr){
            cout << "Enter first student's ID" << endl;
            cin >> id;
            head = new Node{ .id = id, .nextNode = nullptr };
        }

        cout << "\nEnter a choice:" << endl;
        cout << "A) add a student\n" << "R) remove a student\n" << "S) search for a student\n" <<"D) display all student\n" << "I) insert a student\n" << "E) exit\n" << endl;
        cin >> choice;

        if (choice == 'A') {
            cout << "Enter new student's ID" << endl;
            cin >> id;
            add(id, head);
        }
        else if (choice == 'R') {
            cout << "Enter student's ID to be removed" << endl;
            cin >> id;
            remove(id, head);
        }
        else if (choice == 'S') {
            cout << "Enter student's ID" << endl;
            cin >> id;
            search(id, head);
        }
        else if (choice == 'D') {
            cout << "All student's IDs" << endl;
            display(head);
        }
        else if (choice == 'I') {
            cout << "Enter student's ID" << endl;
            cin >> id;
            cout << "Enter wanted position " << endl;
            cin >> position;
            insert(id, head, position);
        } else break;
    }
}

void add(int id, Node* head){

    Node* current = head;
    
    while( current->nextNode != nullptr ){
        current = current->nextNode;
    }
    Node* newNode = new Node{ .id = id, .nextNode = nullptr};
    current->nextNode = newNode;
}

void remove(int id, Node*& head){

    Node* current = head;
    
    if ( head->id == id){
        head = head->nextNode;
        return;
    }

    while(current->nextNode->id != id){
        current = current->nextNode;
    }
    current->nextNode = current->nextNode->nextNode;

}

void insert(int id, Node*& head, int position){
    
    Node* current = head;
    Node* newNode = new Node{ .id = id, .nextNode = nullptr};

    if ( position == 1) {
        newNode->nextNode = head;
        head = newNode;

    }
    else {
        for ( int i = 1; i < position - 1 ; i++){
            current = current->nextNode;
        }

        newNode->nextNode = current->nextNode;
        current->nextNode = newNode;
    }

}

void search(int id, Node* head){
    
    Node* current = head;
    
    while (current->id != id){
        if ( current->nextNode == nullptr){
            cout << "Not found\n";
            break;
        }
        current = current->nextNode;
    }
    if (current->id == id)  cout << "Found\n";
}

void display(Node* head){
 
    Node* current = head;
    while (current->nextNode != nullptr){
        cout << current->id << endl;
        current = current->nextNode;
    }
    cout << current->id << endl;

}
