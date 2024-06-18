import sys
sys.stdin = open('1952_input.txt', 'r')
T=int(input())
for tc in range(1,T+1):
    ticket_prices=list(map(int,input().split()))
    plans=list(map(int,input().split()))
    total=0
    dp=[0]*12
    dp[0]=min(ticket_prices[0]*plans[0],ticket_prices[1])
    dp[1]=min(dp[0]+ticket_prices[0]*plans[1],dp[0]+ticket_prices[1])
    dp[2]=min(dp[1]+ticket_prices[0]*plans[2],dp[1]+ticket_prices[2],ticket_prices[2])
    for i in range(2,11):
        dp[i]=min(dp[i-1]+ticket_prices[0]*plans[i],dp[i-1]+ticket_prices[1],dp[i-3]+ticket_prices[2])
    print(f'#{tc}',min(ticket_prices[3],dp[10]+ticket_prices[0]*plans[11],dp[10]+ticket_prices[1],dp[8]+ticket_prices[2]))
