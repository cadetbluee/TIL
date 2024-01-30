#Baby_gin -> 강사님 정답
#triplit을 먼저 찾고 run을 찾자
import sys
sys.stdin = open("baby_gin_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case} ')