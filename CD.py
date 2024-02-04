N,M=map(int,input().split())
N_list=[]
M_list=[]
for i in range(N):
    N_list.append(int(input()))
for i in range(M):
    M_list.append(int(input()))
last=list(map(int,input().split()))
def binary_search(arr,key):
    start=0
    end=len(arr)-1
    while start<=end:
        middle=(start+end)//2
        if arr[middle]==key:
            return 1
        elif arr[middle]>key:
            end=middle-1
        else:
            start=middle+1
    return 0
result=0
if len(N_list)<len(M_list):
    for i in range(N):
        result+=binary_search(M_list,N_list[i])
else:
    for i in range(M):
        result+=binary_search(N_list,M_list[i])
print(result)