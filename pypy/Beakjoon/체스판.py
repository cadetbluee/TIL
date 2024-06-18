N,M=map(int,input().split())
arr=[input().strip() for _ in range(N)]
chess1=['' for _ in range(8)]
chess2=['' for _ in range(8)]
for i in range(0,8,2):
    chess1[i]+='WB'*(4)
    chess2[i]+='BW'*(4)
for i in range(1,8,2):
    chess2[i]+='WB'*4
    chess1[i]+='BW'*4
ans=[]
for i in range(N-7):
    for j in range(M-7):
        cnt1=0
        for k in range(8):
            for l in range(8):
                if chess1[k][l]!=arr[i+k][j+l]:
                    cnt1+=1
        ans.append(cnt1)
for i in range(N-7):
    for j in range(M-7):
        cnt2=0
        for k in range(8):
            for l in range(8):
                if chess2[k][l]!=arr[i+k][j+l]:
                    cnt2+=1
        ans.append(cnt2)


print(min(ans))