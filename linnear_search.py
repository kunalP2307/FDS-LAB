
def linear_search(array,key):

    for i in range(len(array)):
        if array[i] == key:
            return True;
    return False


if __name__ == '__main__':

    n = (int) (input("Enter the Number of Students Attended Training Program  : "))
    array = [0] * n

    print("Enter the Roll Numbers who Attended the Program : ",end="")
    for i in range(n):
        ele = (int)(input())
        array[i] = ele

    print("Enter Roll to Check Attendance : ",end="")
    key = (int)(input())

    if(linear_search(array,key)):
        print("Given Roll Was Present for the Program")
    else:
        print("Given Roll Was Not Present for the Program")

