import sys
sys.stdin = open("4864_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=input()
    M=input()
    result=0
    if M.find(N)==-1:
        result=0
    else:
        result=1
    print(f'#{test_case} {result}')
