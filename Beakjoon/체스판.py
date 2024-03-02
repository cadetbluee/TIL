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
cnt1=0
for i in range(N):
    for j in range(M):
        if chess1[i][j]!=arr[i][j]:
            cnt1+=1
cnt2=0
for i in range(N):
    for j in range(M):
        if chess2[i][j]!=arr[i][j]:
            cnt2+=1
print(chess1,chess2)
print(cnt1,cnt2)