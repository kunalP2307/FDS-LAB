
def binary_search(array,key):

    l_bound = 0
    u_bound = len(array) - 1

    while l_bound <= u_bound:

        mid = int((l_bound + u_bound) / 2)

        if array[mid] == key:
            return True
        elif array[mid] < key:
            l_bound = mid + 1
        else:
            u_bound = mid - 1

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

    if(binary_search(array,key)):
        print("Given Roll Was Present for the Program")
    else:
        print("Given Roll Was Not Present for the Program")



