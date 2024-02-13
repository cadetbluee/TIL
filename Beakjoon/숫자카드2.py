import sys
sys.stdin=open("10816_input.txt")
from collections import Counter #해시값을 써서 횟수를 저장하기 때문에 훨씬 빠르다
N=int(input())
N_list=list(map(int,input().split()))
# N_dict = {w:N_list.count(w) for w in set(N_list)}
N_dict=Counter(N_list)
M=int(input())
M_list=list(map(int,input().split()))
# M_dict={w:0 for w in input().split()}
for i in M_list:
    # if i in N_list:
    #     print(N_dict[i],end=' ')
    # else:
    #     print(0,end=' ')
    print(N_dict.get(i, 0), end=' ')