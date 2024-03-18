arr=[324,32,22114,16,48,93,422,21,316]
arr.sort()
print(arr)
def binary_search(target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        elif arr[mid]<target:
            low = mid+1
    return -1
def binary_search2(low,high,target):
    #기저조건(언졔까지 재귀가 반복되어야 할까?)
    if low>high:
        return -1
    #다음 재귀 들어가기 전엔 무엇을 해야할까
    mid=(low+high)//2
    if target==arr[mid]:
        return mid
    #다음 재귀 함수 호출
    if target<arr[mid]:
        return binary_search2(low,mid-1,target)
    else:
        return binary_search2(mid+1,high,target)
    #재귀함수에서 돌아왔을 때 어떤 작업을 해야할까


print(f'21 = {binary_search(21)}')
print(f'324 = {binary_search(324)}')
print(f'21 = {binary_search2(0,len(arr),21)}')
print(f'324 = {binary_search2(0,len(arr),324)}')