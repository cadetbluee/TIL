import sys
sys.stdin = open("1979_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,K=map(int,input().split())
    puzzle=[list(map(int,input().split())) for _ in range(N)]
    #print(puzzle)
    count=0
    for i in range(N):

        cnt = 0
        for j in range(N): #0,1,2
            if puzzle[i][j]==1:
                print(f'puzzle[{i}][{j}]={puzzle[i][j]}')
                cnt+=1
                #print(cnt)
        if cnt==K:
            if j==N:
                count+=1
            else:
                if puzzle[i][j+1]==0:
                    count+=1

    for j in range(N ):
        cnt = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                print(f'puzzle[{i}][{j}]={puzzle[i][j]}')
                cnt += 1
        if cnt==K:
            if i == N:
                count += 1
            else:
                if puzzle[i+1][j] == 0:
                    count += 1
    print(count)