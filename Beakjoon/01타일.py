N=int(input())
result=[0]*(N+1)
result[1],result[0]=1,1
for i in range(1,N+1):
    result[i]=result[i-1]+result[i-2]

print(result[N]%15746)