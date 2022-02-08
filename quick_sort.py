
def divide(low_bound,up_bound,array):

    pivot_ele_index = low_bound
    pivot_ele = array[pivot_ele_index]

    while low_bound < up_bound:

        while low_bound < len(array) and array[low_bound] <= pivot_ele:
            low_bound += 1

        while array[up_bound] > pivot_ele:
            up_bound -= 1

        if low_bound < up_bound:
            array[low_bound],array[up_bound] = array[up_bound],array[low_bound]

    array[up_bound],array[pivot_ele_index] = array[pivot_ele_index],array[up_bound]

    return up_bound

def quick_sort(low_bound,up_bound,array):

    if low_bound < up_bound:
        pivot_position = divide(low_bound,up_bound,array)
        quick_sort(low_bound,pivot_position-1,array)
        quick_sort(pivot_position+1,up_bound,array)

def print_array(array):
    print("Scores in Ascending Sorted Order : ")
    for i in range(len(array)):
        print(array[i],end="   ")

if __name__ == '__main__':

    n = (int)(input("Enter the Number of Students : "))

    array = []

    print("Enter Scores : ")
    for i in range(n):
        ele = (float)(input())
        array.append(ele)

    quick_sort(0,len(array) - 1,array)

    print_array(array)