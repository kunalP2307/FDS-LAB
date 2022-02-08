
def minimum(n1,n2):
    if n1 < n2:
        return n1
    return n2

def fibonacci_search(array,key):

    second_last_fib_no = 0
    last_fib_no = 1
    fib_min = second_last_fib_no + last_fib_no
    offset = -1

    while fib_min < len(array):
        second_last_fib_no = last_fib_no
        last_fib_no = fib_min
        fib_min = second_last_fib_no + last_fib_no

    while fib_min > 1:

        i = min(offset + second_last_fib_no, len(array)-1)

        if array[i] < key:
            fib_min = last_fib_no
            last_fib_no = second_last_fib_no
            second_last_fib_no = fib_min - last_fib_no
            offset = i

        elif array[i] > key:
            fib_min = second_last_fib_no
            last_fib_no = last_fib_no - second_last_fib_no
            second_last_fib_no = fib_min - last_fib_no

        else:
            return True

    if last_fib_no == key and array[len(array)-1] == key:
        return True

    return False


if __name__ == '__main__':

    n = int (input("Enter the Number of Students Attended Training Program  : "))
    array = [0] * n

    print("Enter the Roll Numbers who Attended the Program : ",end="")
    for i in range(n):
        ele = int(input())
        array[i] = ele

    print("Enter Roll to Check Attendance : ",end="")
    key = int(input())

    if(fibonacci_search(array,key)):
        print("Given Roll Was Present for the Program")
    else:
        print("Given Roll Was Not Present for the Program")



