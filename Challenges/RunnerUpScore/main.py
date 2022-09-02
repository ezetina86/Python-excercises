"""_summary_
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score.
You are given N scores.
Store them in a list and find the score of the runner-up.

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
"""


def upScore(arr):
    arr.sort()
    litsLength = len(arr)
    while litsLength >= 2:
        if arr[-1] == arr[-2]:
            arr.pop(-1)
            litsLength = len(arr)
            if len(arr) == 1:
                print(arr[0])
        else:
            print(arr[-2])
            break


if __name__ == '__main__':
    isValid = True
    n = int(input())
    if n >= 2 and n <= 10:
        arr = list(map(int, input().split()))
        for element in arr:
            if element >= -100 and element <= 100:
                isValid = True
            else:
                isValid = False
        if isValid == True:
            upScore(arr)
