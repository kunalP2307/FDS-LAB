x	/*
A palindrome is a string of character that„s the same forward and backward. Typically,
punctuation, capitalization, and spaces are ignored. For example, “Poor Dan is in a droop” is
a palindrome, as can be seen by examining the characters “poor danisina droop” and
observing that they are the same forward and backward. One way to check for a palindrome
is to reverse the characters in the string and then compare with them the original-in a
palindrome, the sequence will be identical. Write C++ program with functions-
a) To print original string followed by reversed string using stack
To check whether given string is palindrome or not

*/


#include<iostream>
#include<string.h>
using namespace std;
#define MAX 30

class Stack{

    char string[MAX],stack[MAX];
    int top,length;
    public :
    Stack(){
        top = -1;
        length = 0;
    }

    void getString(){
        cout<<"\n Enter a String: ";
        cin.getline(string,30);
        length= strlen(string);
    }

    void printString(){
        cout<<"\nEntered String : ";
        for(int i=0; string[i] != '\0'; i++){
            cout<<string[i];
        }
    }
    
    void initStack(){
        int i=0;
        int count = 0;
        for(i=0; i < length; i++){
            if(isalpha(string[i])) {   
                push(tolower(string[i]));
                count++;
            }
        }
    
        stack[count] = '\0';
        
    }

    void push(char ch){

        if(top == MAX){
            cout<<"Cannot Push, Stack OverFlow";
            return;
        }

        top++;
        stack[top] = ch;

    }

    bool isPalindrome(){
    
        cout<<"\n Reversed String : ";
        for(int i=0; i<length; i++){
           
            if(!isalpha(string[i]))
                continue;
                
            char ch = pop();
            cout<<ch;
            //cout<<"\n"<<ch<<" "<<string[i];
            if(ch != tolower(string[i]))
                return false;

        }
        return true;
    }
    
    char pop(){

        if(top == -1){
            cout<<"Cannot Pop, Stack Underflow ";
            return '\0';
        }
        
        char ch = stack[top];
        top--;
        return ch;
        
    }

};
int main(){

    Stack stack;
    stack.getString();
    stack.printString();
    stack.initStack();

    if(stack.isPalindrome())
        cout<<"\nGiven String Is Palindrome\n";
    else    
        cout<<"\nGiven String is Not Palindrome\n";
    

    return 0;
}
