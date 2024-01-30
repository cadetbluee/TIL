import sys
sys.stdin = open("9386_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    num=int(input())
    num_list=[]
    for i in range(N):
        num_list.append(num%10)
        num = num//10
    max_c = 0
    cnt = 0
    for i in num_list:
        for j in num_list:
            if i == j and i == 1:
                cnt += 1
                if cnt > max_c:
                    max_c = cnt
            else:
                cnt = 0


    print(f'#{test_case} {max_c}')