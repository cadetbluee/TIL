import sys
sys.stdin = open("1215_input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    arr=[input() for _ in range(8)]
    result=0
    for i in range(8):
        for j in range(8-N+1):
            cnt=0
            for n in range(N):
                if arr[i][j+n]==arr[i][j+N-1-n]:
                    cnt+=1
            if cnt==N:
                result+=1
    for i in range(8):
        for j in range(8-N+1):
            cnt=0
            for n in range(N):
                if arr[j+n][i]==arr[j+N-1-n][i]:
                    cnt+=1
            if cnt==N:
                result+=1
    print(f'#{test_case} {result}')