import sys
sys.stdin = open('5205_input.txt', 'r')


def quickSort(arr, left, right):
    if left < right:
        s = partition(arr, left, right)
        quickSort(arr, left, s - 1)
        quickSort(arr, s + 1, right)
    return arr[N // 2]


def partition(arr, pivot, right):
    x = arr[right]
    i = pivot-1
    for j in range(pivot, right):
        if arr[j]<=x:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right],arr[i+1]
    return i+1

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))

    print(f'#{tc}',quickSort(arr,0,N-1))