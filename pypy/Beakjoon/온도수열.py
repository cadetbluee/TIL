N,K=map(int,input().split())
arr=list(map(int,input().split()))
K_sum=sum(arr[:K])
max_K=K_sum
for i in range(1,N-K+1):
    K_sum=K_sum-arr[i-1]+arr[K+i-1]
    if K_sum>max_K:
        max_K=K_sum
print(max_K)