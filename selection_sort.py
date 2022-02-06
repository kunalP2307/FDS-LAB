def selection_sort(array):

    min_index = 0
    for i in range(len(array)):

        min_index = i
        for j in range(i,len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i],array[min_index] = array[min_index],array[i]

    print("Scores in Ascending Order  : ",end="")
    print_array(array)


def print_array(array):
    for i in array:
        print(i,"  ",end="")


if __name__ == '__main__':

    n = (int)(input("Enter the Number of Students : "))

    array = []

    print("Enter Scores : ")
    for i in range(n):
        ele = (float)(input())
        array.append(ele)

    selection_sort(array)