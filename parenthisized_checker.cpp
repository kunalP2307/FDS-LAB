/*
*   In any language program mostly syntax error occurs due to unbalancing delimiter such as ()... Write C++ program using stack to check whether given expression is well parenthesized or not.
*/

#include<iostream>
#include<string>
# define MAX 25
using namespace std;
char stack[MAX];
int top = -1;

char pop(){
    if(top == -1){
        cout<<"Stack Underflow..";
        return '\0';
    }
    return stack[top--]; 
}

void push(char c){
    if(top == MAX){
        cout<<"Stack Overflow..";
        return;
    }
    stack[++top] = c;
}

bool isEmpty(){
    if(top == -1)
        return true;
    return false;
}

void print_stack(){
    int i = top;

    while (i != -1){
        cout<<stack[i]<<"\t";
        i--;
    }
}

bool checkWellParenthisized(string expression){

    for(int i=0; i<expression.length(); i++){
        
        if(expression[i] == '(' || expression[i] == '{' || expression[i] == '['){
            push(expression[i]);
            continue;
        }
        //print_stack();
        if(isEmpty())
            return false;
        
        char popped_ele = pop();

        switch (expression[i]) {

        case '}':      
            if(popped_ele != '{')
                return false;
            break;
        
        case ')':  
            if(popped_ele != '(')
                return false;
            break;

        case ']':  
            if(popped_ele != '[')
                return false;
            break;
        }
    }

    return isEmpty();
    
}


int main(){
    
    string expression;
    cout<<"Enter Expression  : ";
    cin>>expression;

    if(checkWellParenthisized(expression))
        cout<<"The Given Expression is Well Parenthesized..\n";
    else
        cout<<"The Given Expression is Not Well Parenthesized..\n";
        
    return 0;
}
