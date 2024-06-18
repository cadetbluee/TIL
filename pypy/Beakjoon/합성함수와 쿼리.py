import sys
sys.stdin=open("17435_input.txt")
from sys import stdin
import math
m=int(input())
m_list=list(map(int,input().split()))
table=[[0]*int(math.log2(500000)) for i in range(m)]
for i in range(m):
    table[1][i]=m_list[i]
for k in range(1,int(math.log2(500000))):
    for i in range(m):
        temp=table[k-1][i]
        table[k][i]=table[k-1][temp]
Q=int(input())
for _ in range(Q):
    n,x=map(int,stdin.readline().split())
    if x==m_list[x-1]:
        print(x)
    else:
        for i in range(int(math.log2(500000))-1,-1,-1):
            if (n&(1<<i)):
                x=table[i][x]
        
        print(x)
        for i in range(n):
            x=m_list[x]