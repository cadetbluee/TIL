def factorial(n):
    dp=[0]*n
    dp[0]= 1 
    for i in range(1,n):
        dp[i]=(i+1)*dp[i-1]
    return dp[n-1]
    
n,k=map(int,input().split())
if k==0 or k==n:
    print(1)
else:
    print(int(factorial(n)/(factorial(n-k)*factorial(k))))