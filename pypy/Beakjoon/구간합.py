from sys import stdin
input=stdin.readline
N,M=map(int,input().split())
arr=list(map(int,input().split()))
s_list=[0]*(N+1)
s_list[1]=arr[0]
for i in range(1,N):
    s_list[i+1]=arr[i]+s_list[i]
for _ in range(M):
    i,j=map(int,input().split())
    print(s_list[j]-s_list[i-1])

