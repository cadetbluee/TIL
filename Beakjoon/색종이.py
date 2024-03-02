from sys import stdin
N=int(stdin.readline())
arr=[[0]*1001 for _ in range(1001)]
for idx in range(1,N+1):
    x,y,width,height=map(int, stdin.readline().split())
    for i in range(x,x+width):
        for j in range(y,y+height):
            arr[j][i]=idx

n=1
while n!=N+1:
    cnt=0
    for i in arr:
        for j in i:
            if j==n:
                
                cnt+=1
    n+=1
    print(cnt)