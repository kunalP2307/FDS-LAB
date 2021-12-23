# Name : Kunal Patil
# Enrollment No : SAI&D76


def minMax(studentMarkList):
    minMarks = studentMarkList[0]
    maxMarks = studentMarkList[0]

    # searching for min,max marks obtained and number of absent students

    for i in range(len(studentMarkList)):
        if minMarks == -1:
            minMarks = studentMarkList[i+1]

        if studentMarkList[i] < minMarks:
            minMarks = studentMarkList[i]

        if studentMarkList[i] > maxMarks:
            maxMarks = studentMarkList[i]

    print("Minimum Marks Obtained : ", minMarks)
    print("Maximum Marks Obtained : ", maxMarks)

    return minMarks,maxMarks

def average(studentMarkList):

    absentCount = 0
    totalMarks = 0

    for i in range(len(studentMarkList)):
        if studentMarkList[i] == -1:
            absentCount += 1
        else:
            totalMarks += studentMarkList[i]

    averageMarks = totalMarks / (len(studentMarkList) - absentCount)

    print("Average Marks Obtained :", averageMarks)

    return averageMarks


def absentNumber(studentMarkList):

    absentCount = 0

    for i in range(len(studentMarkList)):
        if studentMarkList[i] == -1:
            absentCount += 1

    print("Total Number of Absent Students :",absentCount)

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

studentMarkList = []
absentCount = 0

n = int(input("Enter the Student Count : "))

print("\n Please Enter -1 If student was absent ")

for i in range(n):
    marks = int(input("Student Marks : "))
    studentMarkList.append(marks)

minMax(studentMarkList)
average(studentMarkList)
absentNumber(studentMarkList)
markWithHighestFreq(studentMarkList)


