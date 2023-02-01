import numpy as np
from math import sqrt


# frobenius norm
def frobenius(Matrix, row, col):
    squared_sum = 0
    for i in range(row):
        for j in range(col):
            squared_sum += Matrix[i][j] * Matrix[i][j]
    return sqrt(squared_sum)


students = []
sum()
for i in range(15):
    student = np.random.randint(25, size=(4, 5))
    students.append((student, frobenius(student, 4, 5)))


def ranking(list):
    return sorted(list, key=lambda x: x[1])


res = ranking(students)
for value in res:
    print(value[0])
    print("Student's norm", value[1])
    print('**************')
