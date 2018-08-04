def diagonal_matrix(matrix):
    return [matrix[index][index] for index in range(matrix.__len__())]


def diagonal_matrix_inverse(matrix):
    return [matrix[index][(matrix.__len__() - 1) - index] for index in range(matrix.__len__())]


array = []
for _ in range(int(input())):
    array.append(list(map(int, input().rstrip().split())))

print(abs(sum(diagonal_matrix(array)) - sum(diagonal_matrix_inverse(array))))
