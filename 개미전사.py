import sys
input=sys.stdin.readline

n=int(input())
food=list(map(int,input().split()))

d=[0]*100

d[0],d[1]=food[0],max(food[0],food[1])

for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+food[i])

print(d[n-1])
