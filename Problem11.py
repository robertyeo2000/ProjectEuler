

def convertFileToMatrix(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    f.close()
    matrix = []
    for line in lines:
        matrix.append(line[0: -1].split(" "))
    return matrix


def calcDownProd(x_start, y_start, matrix):
    return int(matrix[y_start][x_start]) * int(matrix[y_start+1][x_start]) \
           * int(matrix[y_start+2][x_start]) * int(matrix[y_start+3][x_start])


def calcRightProd(x_start, y_start, matrix):
    return int(matrix[y_start][x_start]) * int(matrix[y_start][x_start+1]) \
           * int(matrix[y_start][x_start+2]) * int(matrix[y_start][x_start+3])


def calcDownRightProd(x_start, y_start, matrix):
    return int(matrix[y_start][x_start]) * int(matrix[y_start+1][x_start+1]) \
           * int(matrix[y_start+2][x_start+2]) * int(matrix[y_start+3][x_start+3])


def calcDownLeftProd(x_start, y_start, matrix):
    return int(matrix[y_start][x_start]) * int(matrix[y_start+1][x_start-1]) \
           * int(matrix[y_start+2][x_start-2]) * int(matrix[y_start+3][x_start-3])


matrix = convertFileToMatrix('Problem11Input.txt')
largest = 0
for y_start in range(20):
    for x_start in range(20):
        downProd = 0 if y_start > 16 else calcDownProd(x_start, y_start, matrix)
        rightProd = 0 if x_start > 16 else calcRightProd(x_start, y_start, matrix)
        downRightProd = 0 if x_start > 16 or y_start > 16 else calcDownRightProd(x_start, y_start, matrix)
        downLeftProd = 0 if x_start < 4 or y_start > 16 else calcDownLeftProd(x_start, y_start, matrix)

        largestInCurrentIteration = max(downProd, rightProd, downRightProd, downLeftProd)
        if largest < largestInCurrentIteration:
            largest = largestInCurrentIteration
print(largest)
