lst=[0]*30
for i in range(28):
    n=int(input())
    lst[n-1]=1
for j in range(30):
    if lst[j]==0:
        print(j+1)