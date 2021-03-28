#leetcode ard problem rain fill
from sys import argv
arr=eval(argv[1]);l=len(arr);
count=0
for h in range(1,max(arr)+1):
    f=0
    while arr[f]<h:f+=1
    for r in range(f+1,l):
        if arr[r]>=h:
            count+=r-f-1;
            f=r
print(count)
