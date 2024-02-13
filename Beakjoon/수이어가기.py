N=int(input())
# N=100
max_list=[]
max_cnt=0
for i in range(1,N+1):
    cnt=0
    pre=N
    list_re=[]
    while pre>=0 and i>=0:
        cnt+=1
        list_re.append(pre)
        pre-=i
        if max_cnt<cnt:
            max_cnt=cnt
            max_list=list_re
            if i<0:
                break
        cnt+=1
        list_re.append(i)
        if pre-i>0:
            cnt+=1
            list_re.append(pre-i)
            if max_cnt<cnt:
                max_cnt=cnt
                max_list=list_re
        i-=pre
        if max_cnt<cnt:
            max_cnt=cnt
            max_list=list_re
    # while pre>=0:
    #     cnt+=1
    #     list_re.append(pre-i)
    #     pre-=i
    #     if max_cnt<cnt:
    #         max_cnt=cnt
    #         max_list=list_re
            
print(max_cnt)
print(*max_list)