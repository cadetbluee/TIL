import sys
sys.stdin = open("19640_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    matrix=[[0]*N for _ in range(N)]
    arr_list=[]
    for i in range(N):
        arr_list.extend(arr[i])
    arr_list=sorted(arr_list)

    top, bottom, left, right = 0, N - 1, 0, N - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = arr_list.pop(0)

        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = arr_list.pop(0)

        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = arr_list.pop(0)

            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = arr_list.pop(0)

            left += 1
    # j=1
    # while j<N:
    #     result[j][i-1]=arr_list.pop(0)
    #     j+=1

    print(f'#{test_case}')
    for mat in matrix:
        print(*mat)