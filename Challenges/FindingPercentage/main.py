"""_summary_
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
"""


def percentage(student_marks, query_name):
    sum_mark = 0
    for mark in student_marks[query_name]:
        sum_mark = sum_mark + mark
    avg = (sum_mark / 3)
    print(format(avg, '.2f'))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    percentage(student_marks, query_name)
