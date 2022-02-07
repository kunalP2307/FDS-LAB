
def insertion_sort(array):

    for i in range(1,len(array)):

        temp = array[i]
        j = i - 1

        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = temp

    print(array)

if __name__ == '__main__':

    n = (int)(input("Enter the Number of Students : "))

    array = []

    print("Enter Scores : ")
    for i in range(n):
        ele = (float)(input())
        array.append(ele)


    insertion_sort(array)