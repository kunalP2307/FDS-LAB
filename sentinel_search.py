

def sentinel_search(array,key):

    length = len(array)
    last_ele = array[length-1]
    array[length-1] = key

    i = 0

    while array[i] != key:
        i += 1

    array[length - 1] = last_ele

    if i < length - 1 or array[length - 1] == key:
        return True
    else:
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

    if(sentinel_search(array,key)):
        print("Given Roll Was Present for the Program")
    else:
        print("Given Roll Was Not Present for the Program")

