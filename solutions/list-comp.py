"""
Link to the problem: https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

from itertools import product

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    arr = []
    for i,j,k in product(range(x+1), range(y+1), range(z+1)):
        if i+k+j != n:
            arr.append([i,j,k])
    
    print(arr)
