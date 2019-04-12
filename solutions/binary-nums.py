"""
Link to the problem: https://www.hackerrank.com/challenges/30-binary-numbers/problem
"""

#!/bin/python3
if __name__ == '__main__':
    n = int(input())
    nums = []
    bin_num = bin(n)
    
    ctr = 1
    for i in range(2, len(bin_num)-1):
        if bin_num[i] == bin_num[i+1] == '1':
            ctr+=1
        else:
            nums.append(ctr)
            ctr = 1

    #if the consecutive ones are at the end        
    nums.append(ctr)
    print(max(nums))
