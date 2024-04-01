# N=int(input())
# arr=list(map(int,input().split()))
# rank=[0]*N
# temp=arr
# temp=list(set(temp))
# temp.sort()
# for i in range(N):
#     rank[i]=temp.index(arr[i])
# print(*rank)

arr=list(map(int,input().split()))
arr.sort()
if arr[0]+arr[1] -1 >=arr[2]:
    print(sum(arr))
else:
    print(arr[0]+arr[1]+arr[0]+arr[1] -1 )