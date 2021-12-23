#Name : Kunal Patil
#Enrollment No : SAI&D76


def getMatrix():

    row = int(input("Enter Number of Rows : "))
    column = int(input("Enter Number of Column : "))
    matrix = [[0 for i in range(column)] for j in range(row)]

    for i in range(row):
        for j in range(column):
            number = int(input("Enter Element : "))
            matrix[i][j] = number

    return matrix

def matrixAddition(mat1,mat2):

    if len(mat1) != len(mat2) and len(mat1[0]) != len(mat2[0]):
        print("Addition Not Possible")

    else:
        addition = [[0 for i in range(len(mat1[0]))] for j in range(len(mat1))]

        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                addition[i][j] = mat1[i][j] + mat2[i][j]

    printMatrix(addition)
    return addition


def matrixSubstraction(mat1,mat2):

    if len(mat1) != len(mat2) and len(mat1[0]) != len(mat2[0]):
        print("Subtraction Not Possible")

    else:
        subtraction = [[0 for i in range(len(mat1[0]))] for j in range(len(mat1))]

        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                subtraction[i][j] = mat1[i][j] - mat2[i][j]

    printMatrix(subtraction)
    return subtraction

def matrixTranspose(matrix):

    if len(matrix) != len(matrix[0]):
        print("Transpose is Not Possible")

    else:
        transpose = [[0 for i in range(len(matrix1))] for j in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                transpose[i][j] = matrix[j][i]

    printMatrix(transpose)
    return transpose;

def matrixMultiplication(mat1,mat2):

    if len(mat1[0]) != len(mat2):
        print("Multiplication is Not Possible ")

    else:
        multiplication = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]

        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    multiplication[i][j] += mat1[i][k] * mat2[k][j]

    printMatrix(multiplication)
    return multiplication

def printMatrix(matrix):
    for i in matrix:
        print(i)

    print()


print("For Matrix 1 ")
matrix1 = getMatrix()

print("For Matrix 2 ")
matrix2 = getMatrix()


print("Matrix 1 :")
printMatrix(matrix1)

print("Matrix 2")
printMatrix(matrix2)


print("Addition of Matrices : ")
matrixAddition(matrix1,matrix2)

print("Subtraction of Matrices : ")
matrixSubstraction(matrix1,matrix2)

print("Transpose of Matrix 1 : ")
matrixTranspose(matrix1)

print("Transpose of Matrix 2 : ")
matrixTranspose(matrix2)

print("Multiplication of Matrices : ")
matrixMultiplication(matrix1,matrix2)
