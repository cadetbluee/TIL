import sys

sys.stdin=open('12891_input.txt')
S,P=map(int,input().split())
sequence=list(input())
A,C,G,T=map(int,input().split())

minL={'A':A,'C':C,'G':G,'T':T}
left=0
answer=0
temp={'A':0,'C':0,'G':0,'T':0}
for i in range(P):
    temp[sequence[i]]+=1
if minL['A']<=temp['A'] and minL['C']<=temp['C'] and minL['G']<=temp['G'] and minL['T']<=temp['T']:
    answer+=1
for right in range(P,S):

    temp[sequence[right]]+=1
    temp[sequence[left]]-=1
    left+=1
    if minL['A']<=temp['A'] and minL['C']<=temp['C'] and minL['G']<=temp['G'] and minL['T']<=temp['T']:
        answer+=1
    
print(answer)