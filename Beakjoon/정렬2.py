from sys import stdin
N=int(stdin.readline())
arr=[['','']for _ in range(N)]
for i in range(N):
    arr[i][0],arr[i][1]=stdin.readline().split()
    arr[i][0]=int(arr[i][0])
arr1=sorted(arr,key=lambda x:(x[0],arr.index(x)))
for i in arr1:
    print(*i)