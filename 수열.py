T=int(input())
result=list(map(int,input().split()))
max_c=0
max_t=1
min_t=100000
cnt_m=0
for i in range(T):
    if result[i]>=max_t:
        max_t=result[i]
        cnt_m+=1
cnt_n=0
for i in range(T):
    if result[i]<=min_t:
        min_t=result[i]
        cnt_n+=1
if cnt_m>cnt_n:
    max_c=cnt_m
else:
    max_c=cnt_n
print(max_c)