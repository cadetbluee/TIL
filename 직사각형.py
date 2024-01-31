# sq1=list(map(int,input().split()))
# sq2=list(map(int,input().split()))
# sq3=list(map(int,input().split()))
# sq4=list(map(int,input().split()))
sq1=[1,2,4,4]
sq2=[2,3,5,7]
sq3=[3,1,6,5]
sq4=[7,3,8,6]

square=[[0]*100 for _ in range(100)]
for i in range(100):
    for j in range(100):
        if sq1[0]<j<=sq1[2] and sq1[1]<i<=sq1[3]:
            square[i][j]=1
        if sq2[0]<j<=sq2[2] and sq2[1]<i<=sq2[3]:
            square[i][j]=1
        if sq3[0]<j<=sq3[2] and sq3[1]<i<=sq3[3]:
            square[i][j]=1
        if sq4[0]<j<=sq4[2] and sq4[1]<i<=sq4[3]:
            square[i][j]=1
cnt=0
for i in range(100):
    for j in range(100):
        if square[i][j]==1:
            cnt+=1

print(cnt)