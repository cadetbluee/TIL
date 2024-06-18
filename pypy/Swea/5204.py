import sys
sys.stdin = open('5204_input.txt', 'r')
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    a=list(map(int,input().split()))


    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)


    def merge(left, right):
        global cnt
        left_N = len(left)
        right_N = len(right)
        result = [0] * (left_N + right_N)
        left_i, right_i = 0, 0
        i = 0
        if left[-1] > right[-1]:
            cnt += 1

        while left_i < left_N or right_i < right_N:
            if left_i < left_N and right_i < right_N:
                if left[left_i] <= right[right_i]:
                    result[i] = left[left_i]
                    i += 1
                    left_i += 1
                else:
                    result[i] = right[right_i]
                    i += 1
                    right_i += 1

            elif left_i < left_N:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            elif right_i < right_N:
                result[i] = right[right_i]
                i += 1
                right_i += 1
        return result

    cnt=0
    result=merge_sort(a)[n//2]
    print(f'#{tc} {result} {cnt}')