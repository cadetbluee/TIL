import sys
sys.stdin = open('2112_input.txt')

def check(arr):
    for i in range(W):
        for j in range(D-1):
            arr[j][i]
T=int(input())
for tc in range(1,T+1):
    D,W,K=int(input())
    arr=[list(map(int,input().split())) for _ in range(D)]
    