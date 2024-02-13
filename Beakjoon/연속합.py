n=int(input())
n_list=list(map(int,input().split()))
# stack=[]
# sum_re=0
# pre_sum=sum_re
# for i in range(n):
#     for j in range(n+1):
#         stack.append(sum(n_list[i:j]))
# # stack.append(sum_re)
# print(max(stack))
dp=[0]*n
dp[0]=n_list[0]
for i in range(1,n):
    dp[i]=max(dp[i-1]+n_list[i],n_list[i])
print(max(dp))