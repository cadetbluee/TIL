# def recur(i,s):
#     global cnt
#     if s==K:
#         cnt=min(cnt,i)
#         return
#     elif s>K or i>cnt:
#         return
#     for j in range(N):
#         recur(i+1,s+arr[j])
N,K=map(int,input().split())
arr=[0]*N
for i in range(N):
    arr[i]=int(input())
# idx=[0]*N
# cnt=K/arr[0]
# recur(0,0)
# print(cnt)
arr.sort(reverse=True)
i=0
cnt=0
while K>0:
    if arr[i]<=K:
        K-=arr[i]
        cnt+=1
    else:
        i+=1
print(cnt)