N=int(input())
i=0
while True:
    if i+ sum(int(j) for j in str(i))==N:
        print(i)
        break
    else:
        i+=1