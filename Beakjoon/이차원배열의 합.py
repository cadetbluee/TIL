arr = [[0]*100 for _ in range(100)]
for _ in range(4): # 직사각형 네 개
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] = 1
print(sum(sum(arr,[])))
