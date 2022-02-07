# list to hold the student marks

# assuming student 1 marks as min and man
def getMinMax(studentMarkList):


    for j in range(len(studentMarkList)):
        if studentMarkList[j] == -1:
            continue
        else:
            break

    minMarks = studentMarkList[j]
    maxMarks = studentMarkList[j]

    # searching for min,max marks obtained and number of absent students
    for i in range(j,len(studentMarkList)):
        if studentMarkList[i] == -1:
            continue

        if studentMarkList[i] < minMarks:
            minMarks = studentMarkList[i]

        if studentMarkList[i] > maxMarks:
            maxMarks = studentMarkList[i]

    #print("Minimum Marks Obtained : ", minMarks)
    #print("Maximum Marks Obtained : ", maxMarks)

    return minMarks,maxMarks

def average(studentMarkList):

    totalMarks = 0

    for i in range(len(studentMarkList)):
            totalMarks += studentMarkList[i]

    averageMarks = totalMarks / (len(studentMarkList) - getAbsentCount(studentMarkList))

    print("Average Marks Obtained :", averageMarks)

    return averageMarks


def getAbsentCount(studentMarkList):

    absentCount = 0

    for i in range(len(studentMarkList)):
        if studentMarkList[i] == -1:
            absentCount += 1

    #print("Total Number of Absent Students :",absentCount)

    return absentCount

def markWithHighestFreq(studentMarkList):
    # list for holding the unique marks obtained

    uniqueMarksList = []

    #Finding unique Marks

    for i in range(len(studentMarkList)):
        if studentMarkList[i] not in uniqueMarksList and studentMarkList[i] != -1:
            uniqueMarksList.append(studentMarkList[i])

    # list to hold the frequency of unique marks

    uniqueMarksFrequencyList = [0 for i in range(len(uniqueMarksList))]

    lenOfUniqueMarkList = len(uniqueMarksList)


    # finding the frequency of unique marks
    for i in range(lenOfUniqueMarkList):
        for j in range(n):
            if uniqueMarksList[i] == studentMarkList[j]:
                uniqueMarksFrequencyList[i] += 1

    temp = uniqueMarksFrequencyList[0]
    flag = True

    for i in uniqueMarksFrequencyList:
        if i != temp:
            flag = False
            break

    if(flag):
        return False

    maxFrequency = uniqueMarksFrequencyList[0]
    index = -1
    # finding the maximum Frequency
    for i in range(len(uniqueMarksFrequencyList)):
        if maxFrequency <= uniqueMarksFrequencyList[i]:
            maxFrequency = uniqueMarksFrequencyList[i]
            index = i

    print("Mark with Highest Frequency : ", uniqueMarksList[index])
    print("Frequency Count : ", maxFrequency)

    return uniqueMarksList[index],maxFrequency

# print(uniqueMarksList)
# print(uniqueMarksFrequencyList)
# print(index)

# main

studentMarkList = []
absentCount = 0

n = int(input("Enter the Student Count : "))

print("\n Please Enter -1 If student was absent ")

for i in range(n):
    marks = int(input("Student Marks : "))
    studentMarkList.append(marks)

print("\nStudent Marks\n")
print("Sr No","  Marks")
print("---------------")
for i in range(len(studentMarkList)):
    if studentMarkList[i] == -1:
        print(i+1,".\t\t","A")
    else:
        print(i+1,".\t\t",studentMarkList[i])

min,max = getMinMax(studentMarkList)
print("\nMinimum Marks Obtained : ", min)
print("Maximum Marks Obtained : ", max)

average(studentMarkList)
getAbsentCount(studentMarkList)

if(not markWithHighestFreq(studentMarkList)):
    print("Frequency For all Unique Marks is Same")




