import sys
sys.stdin=open("2805_input.txt")
N,M=map(int,input().split())
n_list=list(map(int,input().split()))
lo,hi=0,max(n_list)
best=0
lumber=0
while hi>=lo:
    lumber=0
    answer=(lo+hi)//2
    for i in n_list:
        if i>answer:
            lumber+=i-answer
    if lumber>=M:
        best = answer
        lo = answer + 1
    else:
        hi=answer-1
print(best)