import sys
sys.stdin = open("1210_input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        j=0
        if arr[j][i]==1:
            ori_i=i
            while j !=99:
                if i!=99 and arr[j][i+1]==1:
                    while i!=99 and arr[j][i+1]==1:
                        i+=1
                    j+=1
                     #print(i)
                elif i!=0 and arr[j][i-1]==1:
                    while i!=0 and arr[j][i-1]==1:
                        i-=1
                    j+=1
                else:
                    j+=1
            if arr[j][i]==2:
                print(f'#{test_case} {ori_i}')

