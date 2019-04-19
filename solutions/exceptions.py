"""
Link to problem: https://www.hackerrank.com/challenges/30-more-exceptions/problem
"""

class Calculator:
    def power(self, base, exp):
        if base < 0 or exp < 0:
            raise Exception("n and p should be non-negative")
        return pow(base, exp)


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans = myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
