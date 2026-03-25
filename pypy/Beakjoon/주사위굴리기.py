import sys
sys.stdin=open('14499_input.txt')
N,M,x,y,K=map(int,input().split())
dice = [0] * 7
board=list(list(map(int,input().split())) for _ in range(N))
K_list=list(map(int,input().split()))
def roll_east(dice):
    temp=dice[:]
    temp[1],temp[3],temp[4],temp[6]=temp[3],temp[6],temp[1],temp[4]
    return temp
def roll_west(dice):
    temp=dice[:]
    temp[1],temp[3],temp[4],temp[6]=temp[4],temp[1],temp[6],temp[3]
    return temp
def roll_north(dice):
    temp=dice[:]
    temp[1],temp[2],temp[5],temp[6]=temp[2],temp[6],temp[1],temp[5]
    return temp
def roll_south(dice):
    temp=dice[:]
    temp[1],temp[2],temp[5],temp[6]=temp[5],temp[1],temp[6],temp[2]
    return temp

for k in K_list:
    nx, ny = x, y

    if k == 1:
        ny += 1
    elif k == 2:
        ny -= 1
    elif k == 3:
        nx -= 1
    elif k == 4:
        nx += 1

    if not (0 <= nx < N and 0 <= ny < M):
        continue
    x, y = nx, ny
    if k == 1:
        dice = roll_east(dice)
    elif k == 2:
        dice = roll_west(dice)
    elif k == 3:
        dice = roll_north(dice)
    elif k == 4:
        dice = roll_south(dice)
        
    if board[x][y] == 0:
        board[x][y] = dice[6]
    else:
        dice[6] = board[x][y]
        board[x][y] = 0

    print(dice[1])