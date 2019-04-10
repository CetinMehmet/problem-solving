"""
     You will be given  integers,  and . There are  words, which might repeat, in word group . 
     There are words belonging to word group . For each  words, check whether the word has appeared in group  or not. 
     Print the indices of each occurrence of  in group . If it does not appear, print .
"""

from collections import defaultdict
defdict = defaultdict(list)
letList=[]

n, m = map(int,input().split())

for i in range(0,n):
    defdict[input()].append(i+1) 

for i in range(0,m):
    letList += [input()]  

for i in letList: 
    if i in defdict:
        print (" ".join( map(str,defdict[i]) ))
    else:
        print (-1)
