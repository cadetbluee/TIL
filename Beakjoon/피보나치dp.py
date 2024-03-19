T=int(input())

def fib_dp(n):
    
    f=[0]*(n+1)
    if n>0:f[1]=1
    if n>1:
        f[2]=1
    for i in range(3,n+1):

        f[i]=f[i-1]+f[i-2]
    return f[n]

for _ in range(T):
    n=int(input())
    if n==0:
        print(1,0)
    else:
        print(fib_dp(n-1),fib_dp(n))