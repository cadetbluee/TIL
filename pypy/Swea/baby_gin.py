import sys
sys.stdin = open("baby_gin_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    list_num = []
    for i in range(6):
        list_num.append(num % 10)
        num = num // 10
    count = [0] * (max(list_num) + 1)
    boolean = 'true'
    for i in list_num:
        count[i] += 1
    for i in range((max(list_num) - 1)):
        if count[i] >= 3:
            count[i] = count[i] - 3

    # print(count)
    for i in range((max(list_num) - 1)):
        if count[i] >= 1:
            if count[i] == count[i + 1] and count[i + 1] == count[i + 2]:
                boolean = 'true'
            else:
                boolean = 'false'
    print(f'#{test_case} {boolean}')