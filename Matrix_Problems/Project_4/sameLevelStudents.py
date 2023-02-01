from typing import Tuple, List

from matplotlib import pyplot as plt
import numpy as np
from math import sqrt
import random


def frobenius(matrix):
    squared_sum = 0
    for vec in matrix:
        squared_sum += vec * vec
    return sqrt(squared_sum)


def ranking(list):
    return sorted(list, key=lambda x: x[1])


def initialGrouping(ranked):
    groups = [[] for _ in range(15)]
    i = 0
    for j in range(15):
        for k in range(15):
            groups[j].append(ranked[i])
            i += 1
    return groups


def get_average(grouping):
    s = 0

    for i in grouping:
        for j in i:
            s += j[1]

    return s / 15


def backTrack(rankedStudents, average, lvl, current, currentList):
    if len(currentList) == 15:  # if the list is filled, than return
        return True

    for stud in (rankedStudents[lvl]):  # choose new student from different groups
        if current + stud[1] > average:
            return False

        current += stud[1]
        currentList.append(stud)

        if backTrack(rankedStudents, average, lvl + 1, current, currentList):  # if student choosing was right, return
            return True
        else:
            current -= stud[1]
            currentList.remove(stud)


def finalGrouping(rankedStudents, average, lvl, current):
    groups = []

    for i in range(15):
        currentList = []
        backTrack(rankedStudents, average, lvl, current, currentList)
        groups.append(currentList)
        for i in range(len(currentList)):
            rankedStudents[14 - i].pop(0)  # take out the student since you already used him/her

    return groups


students = []
for i in range(225):
    Eng = random.randint(60, 80) * 3
    Geo = random.randint(50, 70)
    Math = random.randint(33, 51) * 8
    student = np.array([Eng, Geo, Math])
    students.append((student, frobenius(student)))

ranked = ranking(students)
grouping = initialGrouping(ranked)

groups = finalGrouping(grouping, get_average(grouping) + 100, 0, 0)

scores = []
for group in groups:
    score = 0
    for el in group:
        score += el[1]
    scores.append(score)

labels = list(map(lambda k: k[0], enumerate(groups)))

fig1, ax1 = plt.subplots()
ax1.pie(scores, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')

plt.show()
