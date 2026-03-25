import sys
from collections import deque
import pprint
sys.stdin=open('14891_input.txt')
def turn(str,d):
    if d==1:
        return str[-1]+str[:-1]
    else:
        return str[1:]+str[0]

wheels=[]
for _ in range(4):
    wheels.append(input())
K=int(input())
for _ in range(K):
    idx,d=map(int,input().split())
    q=deque([(idx-1,d)])
    order = []
    visited = [0] * 4
    visited[idx-1] = 1

    while q:
        i, di = q.popleft()
        order.append((i, di))

        # 오른쪽 톱니
        if 0 <= i+1 < 4 and not visited[i+1]:
            if wheels[i][2] != wheels[i+1][6]:
                visited[i+1] = 1
                q.append((i+1, -di))

        # 왼쪽 톱니
        if 0 <= i-1 < 4 and not visited[i-1]:
            if wheels[i][6] != wheels[i-1][2]:
                visited[i-1] = 1
                q.append((i-1, -di))
    for index,direction in order:
        wheels[index]=turn(wheels[index],direction)
# print(wheels)
answer=0
for i,w in enumerate(wheels):
    if w[0]=='1':
        answer+=2**i
print(answer)