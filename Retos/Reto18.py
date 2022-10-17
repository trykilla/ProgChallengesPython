#!/usr/bin/python

# Print the average of the marks array for the student name provided,
# showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sum = 0
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for i in student_marks:
        if i == query_name:
            lista = student_marks[i]
            for j in lista:
                sum += j

    variable = sum/len(lista)
    print("{:.2f}".format(variable))
