"""
    Given an integer, , perform the following conditional actions:

    If  is odd, print Weird
    If  is even and in the inclusive range of  to , print Not Weird
    If  is even and in the inclusive range of  to , print Weird
    If  is even and greater than , print Not Weird
"""
if __name__ == '__main__':
    N = int(input())

    odd = "Weird"
    even = "Not Weird"

    if N % 2 == 1 or (N % 2 == 0 and N >= 6 and N <= 20):
        print(odd)

    elif N % 2 == 0 and (N >= 2 and N <= 5) or (N >= 20):
        print(even)

