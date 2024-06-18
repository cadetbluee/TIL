N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
def area_1(x,y,dir):
    sum_arr=0
    for i in range(x,x+dir[0]):
        for j in range(y-dir[0]-1,y,-1):
            sum_arr+=arr[i][j]
    return sum_arr
def area_2(x,y,dir):
    sum_arr=0
    for i in range(x,x+dir[1]+1):
        for j in range(y,y+dir[1]+1):
            sum_arr+=arr[i][j]
    return sum_arr
def area_3(x,y,dir):
    sum_arr=0
    for i in range(x+dir[0],x+dir[0]+dir[1]+1):
        for j in range(y-dir[0]+dir[1]-1,y-dir[0],-1):
            sum_arr+=arr[i][j]
    return sum_arr
def area_4(x,y,dir):
    sum_arr=0
    for i in range(x+dir[1],x+dir[1]+dir[0]+1):
        for j in range(y+dir[1]-dir[0]-1,y+dir[1],-1):
            sum_arr+=arr[i][j]
    return sum_arr
