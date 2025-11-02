N, B = map(int, input().split())
answer = ''

while N > 0:
    remainder = N % B
    if remainder < 10:
        answer += str(remainder)  # 0~9는 그대로 문자로 변환
    else:
        answer += chr(remainder + 55)  # 10 이상은 A, B, C 등으로 변환
    N //= B

# 결과를 역순으로 출력
print(answer[::-1])
