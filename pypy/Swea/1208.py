import sys
sys.stdin = open("1208_input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    N=int(input())
    box_num=100
    boxes=list(map(int,input().split()))
    boxes=sorted(boxes)
    for i in range(N):
        boxes[box_num-1]-=1
        boxes[0]+=1
        boxes = sorted(boxes)

    print(f'#{test_case} {max(boxes)-min(boxes)}')