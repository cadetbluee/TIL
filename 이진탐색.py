#%%
def binary_search(arr,N,key):
    start = 0 # 구간 초기화
    end = N - 1
    while start <= end: # 검색구간이 유효하면 반복
        middle= (start+end)//2 # 중앙원소 인덱스
        if arr[middle]==key: # 검색 성공
            return middle
        elif arr[middle]>key: # 중앙값이 키보다 크면
            end=middle-1
        else:
            start=middle+1
    return -1
binary_search([1,2,3,6,7,11,12,45],8,12)
#%%
def selection_sort(a,N):
    for i in range(N-1): #구간의 시작 1, 2개의 원소가 남을 때까지
        #구간의 최솟값위치 min_idx,첫 원소를 최소로 가정
        min_idx=i
        for j in range(i+1,N): #실제 최솟값을 찾을 위치 j
            if a[min_idx]>a[j]:
                min_idx=j
        a[min_idx],a[i]=a[i],a[min_idx]
    return

N=5
arr=[-1,3,-2,5,2]
print(arr)
selection_sort(arr,N)