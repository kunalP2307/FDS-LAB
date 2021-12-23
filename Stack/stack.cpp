#include<iostream>
#include<stdio.h>
#include<string.h>
int MAX = 30;
char stack[30];
int top = -1;
using namespace std;

void push(char c){

    if(top != MAX){
        top ++;
        //char upperChar = toupper(c);
        stack[top] = c;
        stack[top+1] = '\0';
    }
}

void printReverseString(){


    cout<<"\nReverse String is : ";

    for(int i = top; i >= 0; i--){
        cout<<stack[i];
    }

}

void isPalindrome(){

    char string[MAX];
    char temp[MAX];
    int i,j;

    for(i = top, j=0; i >= 0; i--,j++)
        string[j] = toupper(stack[i]);

    string[j] = '\0';


    for(i = 0; stack[i] != '\0'; i++)
        temp[i] = toupper(stack[i]);

    if(strcmp(string,temp) == 0)
        cout<<"\n Given Sttring is palindrome ";

    else
        cout<<"\n Given String is not palindrome ";

}

int main(){

    char string[30];

    cout<<"Enter a String : ";
    cin.getline(string,30);

    int i = 0;
    while(string[i] != '\0'){
        push(string[i]);
        i++;
    }

    cout<<"Orignal String "<<string;
    printReverseString();
    isPalindrome();

    return 0;
}
