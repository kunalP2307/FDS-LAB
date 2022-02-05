# A-5 Write a Python program to compute following operations on String:

# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check given string is palindrome or not
# d) To display index of first substring
# e) To count the occurrences of each word in string


def display_word_with_max_length(string):
    temp = ""
    max_len_string = ""

    for i in range(len(string)):

        if string[i].isspace() == False:
            temp += string[i]

        elif len(max_len_string) <= len(temp):
            max_len_string = temp
            temp = ""

    if len(temp) > len(max_len_string):
        return temp
    else:
        return max_len_string


def char_frequency(string,char):

    count = 0

    for i in string:
        if i == char:
            count += 1

    return count

def is_palindrome(string):

    length = len(string)
    mid = (int)(length/2)

    for i in range(mid):
        if string[i] != string[length-i-1]:
            return False

    return True

def index_first_substring(sub,string):

    l_string = len(string)
    l_sub = len(sub)
    flag = True

    for i in range(l_string-l_sub+1):

        for k in range(l_sub):
            if string[i+k] != sub[k]:
                flag = False
                break

        if flag == True:
            return i
        else:
            flag = True

    return -1

def frequency_words(string):

    word_arr = []
    temp = ""

    for i in string:
        if i.isspace() == False:
            temp += i
        else:
            word_arr.append(temp)
            temp = ""

    word_arr.append(temp)

    word_count = {}

    for word in word_arr:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("Word\t|\tFrequency")
    for key,value in word_count.items():
        print(key,"\t|\t",value)

if __name__ == '__main__':

    string = input("Enter Input String : ")
    char = input("Enter a Character to Find its Frequency of Occurrence : ")
    sub = input("Enter Substring to display Index of First Occurrence : ")

    print("Word with longest Length : ",display_word_with_max_length(string))
    print("Frequency of Character ",char," : ",char_frequency(string,char))
    print("Is Given String Palindrome : ",is_palindrome(string))
    print("First Occurrence of Given Substring : ",index_first_substring(sub,string))
    print("Frequency of Each Word In Given String : ")
    frequency_words(string)
