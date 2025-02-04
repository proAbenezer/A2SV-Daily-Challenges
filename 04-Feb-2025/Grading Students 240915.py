# Problem: Grading Students - https://www.hackerrank.com/challenges/grading/problem

import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for index in range(len(grades)):
        if grades[index] < 38:
            continue
        next_multiple = grades[index]
        while True: 
            if next_multiple % 5 == 0:
                break
            next_multiple += 1
        new_grade = next_multiple - grades[index]
        if new_grade < 3:
            grades[index] = next_multiple
    return grades
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
