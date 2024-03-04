from sys import stdin
N=int(stdin.readline())
arr=[['','',0]for _ in range(N)]
for i in range(N):
    arr[i][0],arr[i][1]=stdin.readline().split()
    arr[i][0]=int(arr[i][0])
    arr[i][2]=i
arr1=sorted(arr,key=lambda x:(x[0],x[2]))
for i in range(N):
    print(arr1[i][0],arr1[i][1])