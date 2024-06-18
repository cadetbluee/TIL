import sys
sys.stdin=open("1859_input.txt",encoding="UTF-8")
T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    sale=list(map(int,input().split()))
    money=0
    start=0
    # count=0
    while start<N:
        max_idx=sale.index(max(sale[start:]),start)
        money-=sum(sale[start:max_idx])
        money+=sale[max_idx]*(max_idx-start)
        start=max_idx+1
        # count+=1
        # if count>10000:
        #     a=3

    # for i in range(N-1):
    #     max_price=max(sale[i:])
    #     if sale[i]<=sale[i+1]:
    #         money-=sale[i]
    #         cnt+=1
    #     else:
    #         if sale[i]!=max_price:
    #             money -= sale[i]
    #             cnt += 1
    #         else:
    #             money+=sale[i]*cnt
    #             cnt=0
    # if cnt!=0:
    #     money += sale[N-1] * cnt
    print(f'#{test_case} {money}')