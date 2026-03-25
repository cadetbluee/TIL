import sys

sys.stdin=open('15686_input.txt')

from itertools import combinations
def get_distance(start,end):
    r1,c1=start
    r2,c2=end
    return abs(r1-r2)+abs(c1-c2)

N,M=map(int,input().split())
city=list(list(map(int,input().split())) for _ in range(N))
houses=[]
chickens=[]
for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            houses.append((i,j))
        elif city[i][j]==2:
            chickens.append((i,j))
answer=100000
for selected in combinations(chickens, M):
    total_dis=0
    for house in houses:
        h1,h2=house
        chick_dis=N*N
        for chicken in selected:
            c1,c2=chicken
            dis=get_distance((h1,h2),(c1,c2))
            chick_dis=min(dis,chick_dis)
        total_dis+=chick_dis
    answer=min(total_dis,answer)
print(answer)