# N,M=map(int,input().split())
# arr=[list(map(int,input().split()))for _ in range(N)]
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort(reverse=True)
B.sort()
result=0
for i in range(N):
    result+=A[i]*B[i]
print(result)