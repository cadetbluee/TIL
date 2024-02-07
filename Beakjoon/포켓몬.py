import sys
sys.stdin=open("1620_input.txt","r")
from sys import stdin
N,M=map(int,input().split())
poke_list=[0]*N
poke_reversed = {}
# [].index('dd')
for i in range(N):
    v = stdin.readline().strip()
    poke_list[i]=v
    poke_reversed[v]=str(i+1)
# poke_reversed={v:k for k,v in poke_dict.items()}
result=''
for i in range(M):
    poketmon=stdin.readline().strip()
    if poketmon.isnumeric()==True:
            result+=str(poke_list[int(poketmon)-1])+'\n'
    else:
        result+=poke_reversed[poketmon]+'\n'
print(result)