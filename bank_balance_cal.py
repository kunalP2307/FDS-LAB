# Write a Python program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit) D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300, D 300, W 200, D 100 Then, the output should be: 500


current_balance = 0


def deposit(ammount):
    global current_balance

    current_balance += ammount


def withdrawal(ammount):
    global current_balance

    if current_balance - ammount > 0:
        current_balance -= ammount


if __name__ == '__main__':

    print("Enter Transaction Record : ",end="")
    while True:
        var = input()
        if var == "":
            break
        else :
            transaction_record = var.split(" ")

    for i in range(0,len(transaction_record),2):
        if transaction_record[i] == "D":
            deposit(( int) (transaction_record[i+1]))
        else:
            withdrawal( (int) (transaction_record[i+1]))

    print("Current Available Balance : ",current_balance)
