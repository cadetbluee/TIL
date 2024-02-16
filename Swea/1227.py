import sys
sys.stdin=open("1227_input.txt")
T=10
dirs=[(-1,0),(0,1),(0,-1),(1,0)]
for tc in range(1,T+1):
    n=int(input())
    N = 100
    arr=[list(map(int,input())) for _ in range(N)]
    # arr=[[] for _ in range(N)]
    # print(i_arr)
    # for i in range(N):
    #     for j in range(N):
    #         arr[i].append(i_arr[i][0]%10)
    #         i_arr[i][0]=i_arr[i][0]//10
    # print(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                cur_i, cur_j = [i, j]  # 시작점 찾기
                break
    result=0

    stack=[]
    i_stack=[]
    j_stack=[]
    end = 0
    while True:
        cnt=0

        for d in dirs:
            ni=cur_i+d[0]
            nj=cur_j+d[1]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj]==0:
                    cnt+=1
                    i_stack.append(ni)
                    j_stack.append(nj)
                elif arr[ni][nj]==3:
                    end=1

        if cnt>1:
            stack.append((cur_i,cur_j))
            cur_i= i_stack.pop()
            cur_j=j_stack.pop()
            arr[cur_i][cur_j]=1

        elif cnt==1:
            cur_i = i_stack.pop()
            cur_j = j_stack.pop()
            arr[cur_i][cur_j] = 1
        else:
            if end == 1:
                result = 1
                break
            elif stack:
                cur_i,cur_j=stack.pop()
            else :
                break

    print(f'#{tc} {result}')