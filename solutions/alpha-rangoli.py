"""
Link to the problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
P.S - Pretty bad solution
"""

import string
    
def print_rangoli(size):
    alpha = string.ascii_lowercase

    n = size-1
    lst = []
    width = 4*n + 1
    
    for i in range(n, 0, -1):
        s = "-".join(alpha[n:i:-1] + alpha[i:n] + alpha[n])
        lst.append(s.center(width, "-"))

    for i in range(0, n+1):
        s = "-".join(alpha[n:i:-1] + alpha[i:n] + alpha[n])
        lst.append(s.center(width, "-"))

    for i in lst:
        print(i)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
