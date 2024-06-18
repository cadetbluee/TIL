import sys
sys.stdin = open("1954_input.txt", "r")


def spiral_sequence(n):
    matrix = [[0]*n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix

T = int(input())
for test_case in range(1, T + 1):
    N=int(input())

    num_list=list(range(1,N**2))

    print(f'#{test_case}')
    for i in spiral_sequence(N):
        print(*i)