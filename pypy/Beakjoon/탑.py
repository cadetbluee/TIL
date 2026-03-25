import sys
sys.stdin=open('2493_input.txt')

N=int(input())
towers=list(map(int,input().split()))

answer=[0]*N
stack=[]
for i in range(N):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0] + 1
    else:
        answer[i] = 0
    stack.append((i,towers[i]))

print(*answer)
# for i in range(N-1,-1,-1):
#     print(i)
#     for idx,val in stack:
#         if val<towers[i]:
#             answer[idx]=i+1
            