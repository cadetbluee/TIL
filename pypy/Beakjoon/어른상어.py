import sys
from copy import deepcopy
n, m, k = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(n)]
smell = [[[0,-1]]*n for _ in range(n)]

shark_dir = list(map(int,input().split()))
for i in range(m):
    shark_dir[i] = [shark_dir[i]]
    for _ in range(4):
        shark_dir[i].append(list(map(int,input().split())))

cnt = 0
dir = [(-1,0),(1,0),(0,-1),(0,1)]
temp = 0
while True:
    if temp == m-1 : 
        print(cnt)
        break
    if cnt >= 1000:
        print('-1')
        break

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                smell[i][j] = [k,board[i][j]]

    new_board = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                d, up, down, left, right = shark_dir[board[i][j]-1]
                dir_arr = [up, down, left, right]
                flag = 0
                for p in range(4):
                    dx, dy = dir[dir_arr[d-1][p] - 1]
                    
                    if -1 < i+dx < n and -1 < j+dy < n and smell[i+dx][j+dy] == [0,-1]:
                        
                        if new_board[i+dx][j+dy] == 0:
                            new_board[i+dx][j+dy] = board[i][j]
                            new_board[i][j] = 0
                        
                        else:
                            if new_board[i+dx][j+dy] > board[i][j]:
                                new_board[i+dx][j+dy] = board[i][j]
                            temp += 1
                            new_board[i][j] = 0
                        shark_dir[board[i][j]-1][0] = dir_arr[d-1][p]
                        flag = 1
                        break
                else:
                    
                    for p in range(4):
                        dx, dy = dir[dir_arr[d-1][p] - 1]
                       
                        if -1 < i+dx < n and -1 < j+dy < n and smell[i+dx][j+dy][1] == board[i][j]:
                            new_board[i+dx][j+dy] = board[i][j]
                            new_board[i][j] = 0
                            shark_dir[board[i][j]-1][0] = dir_arr[d-1][p]
                            break

    board = deepcopy(new_board)

    for i in range(n):
        for j in range(n):
            if smell[i][j][1] != -1:
                smell[i][j][0] -= 1
                if smell[i][j][0] == 0:
                    smell[i][j] = [0,-1]

    cnt += 1