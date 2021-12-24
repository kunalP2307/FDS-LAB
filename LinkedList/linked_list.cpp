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
    
    cout<<"\n"<<"PNR No. || Studeent Name  "<<"\n\n";
    while(temp != NULL){
        cout<<temp->pnrNo<<" || "<<temp->studentName<<" -> ";
        temp = temp->next;
    }
    cout<<"NULL";
}

void deleteMember(student* &head,int pnr){

    student* temp = head;
    while(temp->next->pnrNo != pnr){
        temp = temp->next;
    }
    temp->next = temp->next->next;
    cout<<"\nDeletion complete if Record is Presnt ";
    
}

int countMember(student* &head){
    int count = 0;

    student* temp = head;
    while(temp != NULL){
        temp = temp->next;
        count += 1;
    }

    return count;
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

void concatenate(student* &list1,student* &list2){

    student* temp = list1;

    if(list1 == NULL || list2 == NULL){
        cout<<"No data is present in List ";
    }
    else if(list1 == NULL){
        list1 = list2;
        return;
    }
    else if(list2 == NULL){
        return;
    }
    else{
        while(temp->next != NULL){
            temp = temp->next;
        }
        temp->next = list2;
    }
    cout<<"\n Lists Concatenation Complete ! ";

}

student getStudent(){
    
    int pnrNo;
    string studentName;

    cout<<"\nEnter PNR No : ";
    cin>>pnrNo;
    cout<<"Enter student Name : ";
    cin>>studentName;
    student std = student(pnrNo,studentName);
    return std;

}

int main(){

    student* head = NULL;
    student* list2 = NULL;
    
    int rep = 1;
    
      
    do{
        cout<<"\n1-> Add President"<<"\t 2-> Add Member\n";
        cout<<"3-> Add Secretory"<<"\t 4-> Delete President\n";
        cout<<"5-> Delete Member"<<"\t 6-> Delete Secretory\n";
        cout<<"7-> Concatenate Two Lists"<<"\t 8-> Total Number of Member\n";
        cout<<"9-> Display List\n";

        int choice ;
        cout<<"Enter Choice : ";
        cin>>choice;
        student std = student(0,"");

        switch(choice){
            case 1:
                std = getStudent();
                insertPresident(head,std.pnrNo,std.studentName);
                break;

            case 2:
                std = getStudent();
                insertMember(head,std.pnrNo,std.studentName);
                break;

            case 3:
                std = getStudent();
                insertSecretory(head,std.pnrNo,std.studentName); 
                break;  

            case 4:
                deletePresident(head);
                break;

            case 5:
                int pnrToDelete;
                cout<<"Enter Pnr No to Delete Student : ";
                cin>>pnrToDelete; 
                deleteMember(head,pnrToDelete);
                break;

            case 6:
                deleteSecretory(head);
                break;

            case 7:
                concatenate(head,list2);
                break;

            case 8:
                cout<<"Total Number of Members : "<<countMember(head);
                break;

            case 9:
                display(head);
                break;
            
            default:
                break;
            
        }

        cout<<"\n Do want to Continue : [y/n] = [0/1] : ";
        cin>>rep;

    }while(rep == 1);

    


    /*insertPresident(head,121,"patil");
    insertSecretory(head,122,"hskfhjks");
    insertMember(head,123,"kunal");


    insertPresident(list2,121,"abc");
    insertSecretory(list2,122,"rew");
    insertMember(list2,123,"rwererl");
    
    //insertMember(head,124,"abc");
    display(head);
    cout<<"\n";
    cout<<countMember(head);
    cout<<"\n";
    concatenate(head,list2);
    cout<<"After COncatenation :";
    display(head);*/

    /*insertAtTail(head,324,"kunal");
    insertAtTail(head,324,"kunal");
    insertAtTail(head,324,"kunal");
    display(head);
    cout<<"\n";
    insertAtHead(head,123,"Swadeep");
    insertAtHead(head,123,"Swadeep");
    insertAtHead(head,123,"Swadeep");
    
    display(head);
    cout<<"\n";
    deletePresident(head);
    display(head);
    cout<<"\n";
    deleteSecretory(head);
    display(head);*/
    

    return 0;
}


