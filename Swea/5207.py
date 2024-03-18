import sys
sys.stdin = open('5207_input.txt', 'r')

def binary_search(target):

    low=0
    high=N-1
    if_l=0
    if_r=0

    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            if if_l==1:
                return -1
            if_l=1
            if_r=0
            high=mid-1
        elif arr[mid]<target:
            if if_r==1:
                return -1
            if_r=1
            if_l=0
            low = mid+1
        elif arr[mid]==target:
            return 1
    return -1
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=list(map(int,input().split()))
    B=list(map(int,input().split()))
    arr.sort()
    count=0
    for i in range(M):
        if binary_search(B[i])==1:
            count+=1
    print(f'#{tc}',count)
