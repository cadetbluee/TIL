import sys
sys.stdin=open('22251_input.txt')

N,K,P,X=map(int,input().split())

# N개의 층, K개의 자리수, P개 호석이 반전가능,X층에 멈춰있음

floors={0:[1,1,1,0,1,1,1],1:[0,0,1,0,0,1,0],2:[1,0,1,1,1,0,1],3:[1,0,1,1,0,1,1],4:[0,1,1,1,0,1,0],5:[1,1,0,1,0,1,1],6:[1,1,0,1,1,1,1],7:[1,0,1,0,0,1,0],8:[1,1,1,1,1,1,1],9:[1,1,1,1,0,1,1]}
# 다른 층으로 바꿨을 때 바꿔야하는 LED개수
def led_changes(floor1,floor2):
    cnt=0
    for i in range(7):
        if floor1[i]!=floor2[i]:
            cnt+=1
    return cnt
expense=[[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        expense[i][j]=led_changes(floors[i],floors[j])

# print(expense)
# N개의 층을 모두 돌기
cur_floor=str(X).zfill(K)
answer=0
for n in range(1,N+1):
    candidate=(str(n).zfill(K))
    cost=0
    for i in range(K):
        cost+=expense[int(cur_floor[i])][int(candidate[i])]
    if 1<=cost<=P:
        # print(candidate)
        answer+=1
print(answer)
# sign=[]
# for i in range(K,0,-1):
#     sign.append(X%(10**i)//10**(i-1))
# # 바꿀 수 있는 경우의 수..
# for s in sign:
#     cur_led=floors[s]
    
#     for floor,led in floors.items():
#         if floor!=s:
#             change=led_changes(led,cur_led)
#             print(change)
            