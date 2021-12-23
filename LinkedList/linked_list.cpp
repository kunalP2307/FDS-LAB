#include <stdlib.h>
#include <iostream>
#include <string>
int memberCount = 0;
using namespace std;

class student{

    public:
    int pnrNo;
    string studentName;
    student* next;

    student(int no, string name){
        pnrNo = no;
        studentName = name;
        next = NULL; 
    }
};

void insertSecretory(student* &head,int pnr,string name){
    
    student* std = new student(pnr,name);

    if (head == NULL){
        head = std;
        return;
    }

    student* temp = head;
    while( temp->next != NULL){
        temp = temp->next;
    }

    temp->next = std;

}
void insertMember(student* &head,int pnr,string name){

    student* std = new student(pnr,name);
    
    if(head == NULL){
        head = std;
    }
    else{
        student* temp = head;
        while(temp->next != NULL){
            temp = temp->next;
        }
        temp->next = std;
    }
    
}

void insertPresident(student* &head,int pnr,string name){

    student* std = new student(pnr,name);

    if (head == NULL){
        head = std;
    }
    else{
        student* temp = head;
        head = std;
        head->next = temp->next;
    }
}

void display(student* head){
    student* temp = head;

    while(temp != NULL){
        cout<<temp->pnrNo<<" "<<temp->studentName;
        temp = temp->next;
    }
}

void deleteMember(student* &head,int pnr){
    student* temp = head;
    while(temp->next->pnrNo != pnr){
        temp = temp->next;
    }
    temp->next = temp->next->next;
    
}

void deletePresident(student* &head){
    
    if(head == NULL){
        return;
    }
    if(head->next == NULL){
        deletePresident(head);
    }
    
    student* toDelete = head;
    head = head->next;
    delete toDelete;
    
}

void deleteSecretory(student* &head){
    
    if(head == NULL){
        return;
    }
    
    if(head->next == NULL){
        deletePresident(head);
        return;
    }
    
    student* temp = head;
    student* std;
    while(temp->next != NULL){
        std = temp;
        temp = temp->next;
    }
    
    std->next = NULL;
    delete temp;
    
}

int main(){

    student* head = NULL;
    insertPresident(head,121,"patil");
    insertSecretory(head,120,"vevek");
    insertMember(head,122,"hskfhjks");
    insertMember(head,123,"kunal");
    insertMember(head,124,"abc");


    /*insertAtTail(head,324,"kunal");
    insertAtTail(head,324,"kunal");
    insertAtTail(head,324,"kunal");
    display(head);
    cout<<"\n";
    insertAtHead(head,123,"Swadeep");
    insertAtHead(head,123,"Swadeep");
    insertAtHead(head,123,"Swadeep");*/
    
    display(head);
    cout<<"\n";
    deletePresident(head);
    display(head);
    cout<<"\n";
    deleteSecretory(head);
    display(head);
    

    return 0;
}


