"""
Link to problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
"""

if __name__ == "__main__":
    n = int(input())
    names, dic = [], {}

    [names.append(tuple(map(str, input().split()))) for _ in range(n)]
    dic.update(names)

    for i in range(0,n):
        try:
            search = str(input())
            if search in dic:
                print(search+"="+dic[search])
            else:
                print("Not found")
        except:
            break
