# def check(i,j):
#     l=len(arr[i][j])
#     m,s,hol,jjak=0,0,1,1
#     while arr[i][j]:
#         a=arr[i][j].pop()
#         m+=a[0]
#         s+=a[1]
#         if a[2]%2==1:
#             jjak=0
#         else:
#             hol=0
#     m=m//5
#     if m==0: 
#         arr[i][j]=[] 
        
#     else:
#         s=s//l
#         if hol==1 or jjak==1:
#             for d in range(0,8,2):
                
#                 arr[i][j].append((m,s,d))
#         else:
#             for d in range(1,9,2):
                
#                 arr[i][j].append((m,s,d))
# def move(i,j):
#     nr=(i+dirs[d][0]*s)%N
#     nc=(j+dirs[d][1]*s)%N
#     arr[nr][nc].append((m,s,d))
# N,M,K=map(int,input().split())
# dirs=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
# arr=[[[]for _ in range(N)] for _ in range(N)]
# for _ in range(M):
#     r,c,m,s,d=map(int,input().split())
#     arr[r-1][c-1].append((m,s,d))
# for _ in range(K):
#     for i in range(N):
#         for j in range(N):
#             while arr[i][j]:
#                 m,s,d=arr[i][j].pop()
#                 move(i,j)
#     for i in range(N):
#         for j in range(N):
#             if len(arr[i][j])>=2: check(i,j)
        
# result=0
# for a in arr:
#     for i in a:
#         if i:
#             for j in i:
#                 result+=j[0]
            
        
# print(result)

N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

# 0 ~ 7까지의 방향
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    # 이동 할 위치를 저장할 배열
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] != []:
                # 위치 이동
                for m, s, d in arr[i][j]:
                    r = (i + dir[d][0] * s) % N
                    c = (j + dir[d][1] * s) % N
                    board[r][c].append([m, s, d])

    # 이동한 파이어볼들을 체크
    for i in range(N):
        for j in range(N):
            # 한 위치에 파이어볼이 2개 이상인 경우
            if len(board[i][j]) >= 2:
                mass = 0;speed = 0;check1 = 0;check2 = 0
                # 질량과 속도 구하기 + 홀짝 체크
                for m, s, d in board[i][j]:
                    mass += m
                    speed += s
                    if (d % 2)==0:check1 += 1
                    if (d % 2): check2 += 1

                mass //= 5
                # 질량이 0인 경우 위치를 초기화하고 continue
                if mass == 0:
                    board[i][j] = []
                    continue
                speed //= len(board[i][j])
                # 홀수나 짝수인 경우
                if check1 == len(board[i][j]) or check2 == len(board[i][j]):
                    board[i][j] = []
                    for d in [0, 2, 4, 6]:
                        board[i][j].append([mass, speed, d])
                # 그 외의 경우
                else:
                    board[i][j] = []
                    for d in [1, 3, 5, 7]:
                        board[i][j].append([mass, speed, d])
    # 2차원 배열를 통해
    arr = [lst[:] for lst in board]

ans = 0
# 파이어볼이 있는 경우 질량 구하기
for i in range(N):
    for j in range(N):
        if arr[i][j] != []:
            for m, s, d in arr[i][j]:
                ans += m

print(ans)