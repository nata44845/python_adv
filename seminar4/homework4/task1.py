# Задание 1
# Напишите функцию для транспонирования матрицы

def transp(matrix: list):
    new_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i]=matrix[i][j]
    return new_matrix

data = [[1,2,3,223],[4,5,6,18],[7,8,9,100]]

print(transp(data))

