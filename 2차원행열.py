N,M=map(int,input().split())
N_list=[list(map(int,input().split())) for _ in range(N)]
N2_list=[list(map(int,input().split())) for _ in range(N)]
new_list=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        new_list[i][j]=N_list[i][j]+N2_list[i][j]

for i in range(N):
    print(*new_list[i])
    
arr=[list(map(int,input().split())) for _ in range(9)]
max_list=[0]*2
max_cnt=0
for i in range(9):
    for j in range(9):
        if arr[i][j]>max_cnt:
            max_cnt=arr[i][j]
            max_list[0]=i
            max_list[1]=j
print(max_cnt)
print(max_list[0]+1,max_list[1]+1)
#%%
arr1='ABCDE'
arr2='abcde'
arr3='0134'
arr4='FGHIJ'
arr5='fghij'

for i in range(len(arr1)):
    new_arr=arr1[i]+arr2[i]+arr3[i]+arr4[i]+arr5[i]
    new_arr = new_arr.replace(" ", "")  # Remove spaces
    print(new_arr, end='')
print()
# %%
arr = []
len_arr = []
ans=list()
for i in range(5):
    line = list(input())
    arr.append(line)
    len_arr.append(int(len(line)))

for k in range(max(len_arr)):
    for j in range(5):
        if k <= (len_arr[j]-1):
            ans.append(arr[j][k])

for p in range(int(len(ans))):
    print(ans[p], end='')
# %%
N=int(input())
squares=[list(map(int,input().split())) for _ in range(N)]
arr=[[0]*100 for _ in range(100)]
cnt=0
for c in range(N):
    for i in range(squares[c][1],squares[c][1]+10):
        for j in range(squares[c][0],squares[c][0]+10):
            if arr[i][j]==0:
                arr[i][j]=1
            else:
                cnt+=1
print(cnt)
# %%
