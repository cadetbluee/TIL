bingo=[list(map(int,input().split())) for _ in range(5)]
ans=[list(map(int,input().split())) for _ in range(5)]
count=0
for i in range(5):
    for j in range(5):
        count+=1
        bin=0
        for k in range(5):
            for l in range(5):
                if ans[i][j] ==bingo[k][l]:
                    bingo[k][l]=0
                    bin=1
                    break
            if bin==1:
                break
        cnt=0
        for k in range(5):
            sero=0
            garo=0
            degak1=0
            degak2=0
            for l in range(5):
                if bingo[l][k]==0:
                    sero+=1
                if bingo[k][l]==0:
                    garo+=1
                if bingo[l][l]==0:
                    degak1+=1
                if bingo[l][4-l]==0:
                    degak2+=1
            if sero==5:
                cnt+=1
            if garo==5:
                cnt+=1
            if k==0 and degak1==5:
                cnt+=1
            if k==0 and degak2==5:
                cnt+=1

        if cnt>=3:
            break
    if cnt>=3:
        break
print(count)