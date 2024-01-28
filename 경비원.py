garo,sero=map(int,input().split())
store_num=int(input())
store_direction=[]
store_length=[]
for i in range(store_num):
    a,b=map(int,input().split())
    store_direction.append(a)
    store_length.append(b)
my_di,my_len=map(int,input().split())
sum_t=0
for i in range(store_num):
    if store_direction[i]==my_di:
        sum_t+=abs(my_len-store_length[i])