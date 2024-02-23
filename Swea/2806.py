import sys
sys.stdin = open("2806_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
