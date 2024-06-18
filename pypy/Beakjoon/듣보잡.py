import sys
sys.stdin=open("1764_input.txt")
from sys import stdin
N,M=map(int,input().split())
N_set=set()
for i in range(N):
    name=stdin.readline().strip()
    N_set.add(name)
M_set=set()
for i in range(M):
    name=stdin.readline().strip()
    M_set.add(name)
result_set=N_set&M_set
result_set=sorted(result_set)
print(len(result_set))
for i in result_set:
    print(i)