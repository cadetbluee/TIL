N,M=map(int,input().split())
N_list=[list(map(int,input().split())) for _ in range(N)]
N2_list=[list(map(int,input().split())) for _ in range(N)]
new_list=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        new_list[i][j]=N_list[i][j]+N2_list[i][j]

for i in range(N):
    print(*new_list[i])