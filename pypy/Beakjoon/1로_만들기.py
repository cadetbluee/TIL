import sys
sys.stdin=open('1463_input.txt')
N = int(input())
dp=[0]*(N+1)
# def make1(n):
#     global dp
#     if n>3 and not dp[n-1]:
#         if n%3==0  and make1(n-1)>=make1(n//3):
#             dp[n-1]=make1(n//3)+1
#         elif n%2==0 and make1(n-1)>=make1(n//2):
#             dp[n-1]=make1(n//2)+1
#         else:
#             dp[n-1]=make1(n-1)+1
#     return dp[n-1]
for i in range(2,N+1):
    if i%3==0 and i%2==0:
        dp[i]=min(dp[i-1],dp[i//3],dp[i//2])+1
    elif i%3==0:
        dp[i]=min(dp[i-1],dp[i//3])+1
    elif i%2==0:
        dp[i]=min(dp[i-1],dp[i//2])+1
    else:
        dp[i]=dp[i-1]+1
print(dp[N])