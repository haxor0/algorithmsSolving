A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
matrix=[]

def multiplicationLineColumn(line,column):
    try:
        sizeLine=len(line)
        sizeColumn=len(column)
        if(sizeLine!=sizeColumn):
            raise ValueError("Exception")
        res = sum([line[i] * column[i] for i in range(sizeLine)])
        return res
    except ValueError:
        print("sould have the same len ligne & colonne")

def  getColumn(matrix,numColumn):
    size=len(matrix)
    column= [matrix[i][numColumn-1] for i in range(size)]
    return column

def getLine(matrix,numLine):
    line = matrix[numLine-1]
    return line

for i in range(len(A)):
    matrix.append([])
    for j in range(len(B)):
        matrix[i].append(multiplicationLineColumn(getLine(A,i+1),getColumn(B,j+1)))

print(matrix)