import sys
sys.stdin = open("1961_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=[['']*3 for _ in range(N)]

    for i in range(N):
        for l in range(N-1,-1,-1):
            result[i][0]+=str(arr[l][i])

    for k in range(N-1,-1,-1):
        i = 0
        for j in range(N-1,-1,-1):
            if i==N:
                pass
            else:
                result[i][1] += str(arr[j][k])
                i+=1
    i = 0
    for k in range(N - 1, -1, -1):
        for l in range(N):
            if i==N:
                pass
            else:
                result[i][2] += str(arr[l][k])
        i += 1

    print(f'#{test_case}')
    for i in range(N):
        print(*result[i])