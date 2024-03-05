# n=int(input())

def fib_dp(n):
    
    f=[0]*(n+1)
    f[1],f[2]=1,1
    for i in range(3,n+1):

        f[i]=f[i-1]+f[i-2]
    return f[n]

#print(fib_dp(n),n-2)
n,k=map(int,input().split())
print(fib_dp(n)/(fib_dp(n-k)*fib_dp(k)))