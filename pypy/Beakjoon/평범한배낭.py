import sys

sys.stdin=open('12865_input.txt')


N,K=map(int,input().split())

goods=[tuple(map(int,input().split())) for _ in range(N)]
max_value=0
dp=[0]*(K+1)
for weight,value in goods:
    for i in range(K,weight-1,-1):
        dp[i]=max(dp[i],dp[i-weight]+value)

print(dp)