import sys
sys.stdin=open('3499_input.txt')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=input().split()
    result=[]
    if N%2==0:
        arr1=arr[:N//2]
        arr2=arr[N//2:]
    else:
        arr1 = arr[:N // 2 + 1]
        arr2 = arr[N // 2 + 1:]
    for i in range(len(arr2)):
        result.append(arr1[i])
        result.append(arr2[i])
    if N%2==1:
        result.append(arr1[-1])
    print(f'#{tc}',*result)