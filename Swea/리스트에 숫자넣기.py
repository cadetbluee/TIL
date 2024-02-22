N=int(input())
arr=[[0]*7 for i in range(2)]
for i in range(N,N+4):
    arr[0][i-N]=i
for j in range(N,N-4,-1):
    arr[1][6-N+j]=j
print(arr[0])
print(arr[1])