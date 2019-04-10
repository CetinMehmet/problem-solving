"""
    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
    You are given scores. Store them in a list and find the score of the runner-up.
"""

def runUpScore(arr):
    highest, secHigh = max(arr[0],arr[1]), min(arr[0], arr[1])
    for i in range(2,len(arr)): 
        if arr[i] > highest: 
            secHigh = highest
            highest = arr[i] 
        else: 
            if arr[i] > secHigh and arr[i] < highest: 
                secHigh = arr[i] 
    print(secHigh)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    runUpScore(arr)
