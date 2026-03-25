import sys
sys.stdin=open('20055_input.txt')
from collections import deque
N,K=map(int,input().split())
belt=deque(map(int,input().split()))
robot = deque([0] * N)
countZero=0
answer=0

while True:
    answer+=1
    # print(robots)
    # 1번 > 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[-1]=0
    # 2번 > 가장 먼저 벨트에 올라간 로봇부터 한칸 옮길 수 있다면 이동
    for i in range(N-2,-1,-1):
            if robot[i]==1 and robot[i+1]==0 and belt[i+1]>0:
                robot[i]=0
                robot[i+1]=1
                belt[i+1]-=1
                if belt[i+1]==0:
                    countZero+=1
            
    robot[-1]=0
    # 3번 > 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올리기
    if belt[0]>0:
        robot[0]=1
        belt[0]-=1
        if belt[0]==0:
            countZero+=1
    # 4번 > 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
    if countZero>=K:
        break
    
print(answer)