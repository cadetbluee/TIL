from collections import deque
N=int(input())
arr=list(map(int,input().split()))
Q=deque()
Q.append(1)
while Q:
    num=Q.popleft()
    Q.append(arr.pop(num-1))
    print(Q)

