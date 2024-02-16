import sys
sys.stdin=open("4408_input.txt")
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    for _ in range(N):
        cur,dep=map(int,input().split())
