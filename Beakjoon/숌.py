def find_end_of_world_number(n):
    count = 0  # 연속된 6의 개수를 세는 변수
    num = 666  # 종말의 수로 시작
    
    while True:
        if '666' in str(num):  # 만약 해당 숫자에 '666'이 포함되어 있다면
            count += 1  # count를 1 증가시킴
            if count == n:  # count가 입력으로 주어진 n과 같다면
                return num  # 해당 숫자를 반환
        num += 1  # 다음 숫자로 이동

# 입력 받기
N = int(input("N을 입력하세요: "))

# N번째 영화의 제목에 들어간 수 출력
print(find_end_of_world_number(N))
