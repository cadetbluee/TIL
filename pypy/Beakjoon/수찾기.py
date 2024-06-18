N=int(input())
A=list(map(int,input().split()))
A.sort()
M=int(input())
B=list(map(int,input().split()))
def binary_search(arr,target):
    start=0
    end=len(arr)-1
    while start<=end:
        middle=(start+end)//2
        if target==arr[middle]:
            return 1
        elif target>arr[middle]:
            start=middle+1
        else:
            end=middle-1
    return 0
for i in B:
    print(binary_search(A,i))