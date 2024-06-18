import sys
sys.stdin = open('./1979_input.txt')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,K=map(int,input().split())
    puzzle=[list(map(int,input().split())) for _ in range(N)]
    #print(puzzle)
    count=0
    # for i in range(N):
    #     for j in puzzle[i]:
    #         cnt=0
    #         for p in j:
    #             if p=='1':
    #                 cnt+=1
    #                 #print(cnt)
    #         if cnt==K:
    #             count+=1
    for i in range(N):
        for j in range(N-K+1):
            cnt=0
            for p in range(K):
                if puzzle[i][j+p]==1:
                #print(f'puzzle[{i}][{j}]={puzzle[i][j]}')
                    cnt+=1
                #print(cnt)
            if cnt==K:
                if N==K:
                    count+=1
                elif j+K-1==N-1:
                    if puzzle[i][j-1]==0:
                        count+=1
                elif j==0:
                    if puzzle[i][j+K]==0:
                        count+=1
                elif puzzle[i][j-1]==0 and puzzle[i][j+K]==0:
                    count+=1
            

    for j in range(N):
        for i in range(N-K+1):
            cnt=0
            for p in range(K):
                if puzzle[i+p][j]==1:
                #print(f'puzzle[{i}][{j}]={puzzle[i][j]}')
                    cnt+=1
                #print(cnt)
            if cnt==K:
                if N==K:
                    count+=1
                elif i+K-1==N-1:
                    if puzzle[i-1][j]==0:
                        count+=1
                elif i==0:
                    if puzzle[i+K][j]==0:
                        count+=1
                elif puzzle[i-1][j]==0 and puzzle[i+K][j]==0:
                    count+=1
    print(f'#{test_case} {count}')