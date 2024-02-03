T=int(input())
result=list(map(int,input().split()))
max_c=1
cnt_m=1
for i in range(1,T):
    if result[i]>=result[i-1]:
        cnt_m+=1
        if cnt_m>max_c:
            max_c=cnt_m
    else:
        cnt_m=1
cnt_n=1
for i in range(1,T):
    if result[i]<=result[i-1]:
        cnt_n+=1
        if cnt_n>max_c:
            max_c=cnt_n
    else:
        cnt_n=1

print(max_c)