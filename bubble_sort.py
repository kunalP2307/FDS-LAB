
def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

    print("Percentages in Ascending Sorted Order : ",end="")
    print_array(array)

def print_array(array):

    for i in range(len(array)):
        print(array[i],"  ",end="")

def print_top_five_score(array):

    print("\nTop 5 Scores : ",end="")

    for i in(range(len(array)-1,len(array)-6,-1)):
        print(array[i]," ",end="")


if __name__ == '__main__':

    n = (int)(input("Enter Number of Students : "))

    array = []

    print("Enter Scores : ")
    for i in range(n):
        ele = (float)(input())
        array.append(ele)

    bubble_sort(array)
    print_top_five_score(array)